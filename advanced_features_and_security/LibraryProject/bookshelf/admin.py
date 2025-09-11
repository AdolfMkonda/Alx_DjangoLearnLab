from django.contrib import admin

from .models import Book, CustomUser, CustomUserManager, AbstractUser, BaseUserManager
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year')
    list_filter = ('publication_year')
    search_fields = ('title', 'author')
    list_per_page = 30

admin.site.register(CustomUser, CustomUserAdmin)
