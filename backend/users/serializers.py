from rest_framework import serializers

from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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
            "refesh": str(refresh),
        }
        
            
            