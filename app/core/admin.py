from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
''' recommended convention for converting strings in python
to human readable text it pass throug translation engin
for multiple languages it will make it a lot easier
'''
from django.utils.translation import gettext as _

from core import models


class UserAdemin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', )}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('important dates'), {'fields': ('last_login', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
         }),
    )


admin.site.register(models.User, UserAdemin)
