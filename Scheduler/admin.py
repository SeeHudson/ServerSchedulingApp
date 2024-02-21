from .models import AppUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserCreationForm, AppUserChangeForm
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = ('uID', 'email', 'is_staff', 'is_active',)
    list_filter = ('uID', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('uID', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('uID', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('uID', 'email',)
    ordering = ('uID', 'email',)


admin.site.register(AppUser, AppUserAdmin)

