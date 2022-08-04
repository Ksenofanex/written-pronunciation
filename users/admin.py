from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "is_active",
        "is_staff",
    ]

    add_fieldsets = (
        (
            "Username and Email",
            {
                "fields": (
                    "username",
                    "email",
                ),
            },
        ),
        (
            "Password",
            {
                "fields": ("password1", "password2"),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_superuser"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
