from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display=(
        "id",
        "username",
        "email",
        "role",
        "is_staff",
        "is_active",
        "created_at",
    )
    
    list_filter= (
        "role",
        "is_staff",
        "is_active",
    )
    
    search_fields = (
        "username",
        "email",
        "phone",
    )
    
    ordering = ("-created_at",)
    
    fieldsets = UserAdmin.fieldsets + (
    (
            "Additional Information",
        {
            "fields": (
                "profile_picture",
                "phone",
                "bio"
                "role",
                "created_at",
                "updated_at",
                
            )
        },
        
      ),
    )
    
    readonly_fields = (
        "created_at",
        "updated_at",
    )
