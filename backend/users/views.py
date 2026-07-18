from django.shortcuts import render


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.utils import extend_schema


# serializers
from .serializers import RegisterSerializer
from .serializers import LoginSerializer, LogoutSerializer, ChangePasswordSerializer


# Create your views here.
class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            
            user = serializer.save()
            
            return Response(
                {
                    "status": "success",
                    "message": "User Registered Successfully",
                    "data": RegisterSerializer(user).data
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors
                
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        

# login 
class LoginView(APIView):
    
    serializer_class = LoginSerializer
    
    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            
            return Response(
                {
                    "status": "success",
                    "message": "Login Successful",
                    "data": serializer.validated_data
                },
                status=status.HTTP_200_OK
            )
            
        return Response(
            {
                "status": "error",
                "error": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
# profile
class ProfileView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        serializer = RegisterSerializer(request.user)
        
        return Response(
            {
                "status": "success",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer
    
    def post(self, request):
        
        serializer = LogoutSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(
            {
                "status" : "success",
                "message" : "Logout Successful"
            },
            status=status.HTTP_200_OK
        )
        
class ChangePasswordView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def post(self, request):
        
        serializer = ChangePasswordSerializer(
            data = request.data,
            context= {"request": request}
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {
                "status": "success",
                "massage": "Password changed successfully"
            },
            status=status.HTTP_200_OK
        )
        
        