from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView # for token refresh

from .views import (
    RegisterView, 
    LoginView, 
    ProfileView, 
    LogoutView, 
    ChangePasswordView,
    ForgotPasswordView,
    VerifyOTPView,
    RestPasswordView,
    
    )

urlpatterns = [
    path("register/", RegisterView.as_view(),name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", ProfileView.as_view(), name="profile"),
    
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("chenge-password/",ChangePasswordView.as_view(), name="change-password"),
    path("forgot-password/",ForgotPasswordView.as_view(), name="forgot-password"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path("reset-password/", RestPasswordView.as_view(), name="reset-password"),
]

