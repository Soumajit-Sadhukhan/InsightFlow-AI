from rest_framework import serializers

from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# for otp
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
import random


import random

#serializers convard json
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "bio",
            "role",
        
        )
        
        # for Security 
        extra_kwargs ={
            "password": {"write_only": True}
        }
        
    # password hash
    def create(self, validated_data):
        password = validated_data.pop("password")
            
        user = User(**validated_data)
        user.set_password(password)
            
        user.save()
            
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    #requre
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(
            username = username,
            password = password
        )
        
        # miss match
        if not user:
            raise serializers.ValidationError("Invalid username or password")

        refresh = RefreshToken.for_user(user) # jwt token create 
        
        return{
            "user": RegisterSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        
        
#logout
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
            
    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs 
    def save(self):
        token = RefreshToken(self.token)
        token.blacklist()   
        
 #chenge password       
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        user = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError(
                {"old_password": "Old Password is Incorrect"}
            )
        return attrs
    def save(self):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        
class ForgotPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    
    def validate(self, attrs):
        email = attrs["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "User with this email does not exist"
            )
            
        otp = str(random.randint(100000, 999999))
        
        user.otp=otp
        user.otp_created_at = timezone.now()
        user.save()
        
        send_mail(
            subject="InsightFlow AI Password Reset OTP",
            message=f"Your OTP is {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
             fail_silently=False,
        )
        
        return attrs
    
    
class VerifyOTPSerializer(serializers.Serializer):
        
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
        
        
    def validate(self, attrs):
            
        email = attrs["email"]
        otp = attrs["otp"]
            
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
            
            
        if user.otp != otp:
            raise serializers.ValidationError("Invalid OTP")
        return attrs
    
class ReserPasswordSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email= attrs["email"]
        otp = attrs["otp"]
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not  found")
        
        if user.otp != otp:
            raise serializers.ValidationError("Invalid OTP")
        self.user = user
        
        return attrs
    def save(self):
        new_password = self.validated_data["new_password"]
        
        self.user.set_password(new_password)
        
        #otp clear
        
        self.user.otp = None
        self.user.otp_created_at = None
        
        self.user.save()