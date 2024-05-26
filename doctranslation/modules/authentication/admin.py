from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import APIAuthToken, User

admin.site.unregister(Group)


@admin.register(APIAuthToken)
class APIAuthTokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'user', 'created')
    readonly_fields = ('key', 'created')
    raw_id_fields = ('user',)
    ordering = ('-created',)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = (
        'id', 'email', 'is_active',
        'is_superuser', 'last_accessed_at',
    )
    list_filter = ('is_active', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('created_at', 'last_accessed_at')}),
    )

    readonly_fields = ('user_permissions', 'created_at', 'last_accessed_at')
    ordering = ('id',)
    search_fields = ('email',)
