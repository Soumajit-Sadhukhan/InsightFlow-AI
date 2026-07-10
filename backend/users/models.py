from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    ROLE_CHOICES =(
        ("user","User"),
        ("admin","Admin"),
    )
    
    #set profile pic
    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )
    
    #phon number
    phone = models.CharField(
        max_length=15,
        blank=True
    )
    
    # file detalse
    bio = models.TextField(
        blank=True
    )
    
    # check it is user or not
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default="user"
    )
    
    # profile cteated taiming
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    
    
    # updated taiming
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    # Email Verification
    is_verified = models.BooleanField(default=False)
    
    otp= models.CharField(
        max_length=6,
        blank=True,
        null=True
    )
    
    otp_created_at = models.DateTimeField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.username
    
    
    