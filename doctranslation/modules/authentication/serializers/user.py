from zoneinfo import ZoneInfo

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from doctranslation.modules.common.constants import APP_TIME_ZONE


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()
    last_accessed_at = serializers.DateTimeField(default_timezone=ZoneInfo(APP_TIME_ZONE))

    class Meta:
        model = get_user_model()
        read_only_fields = (
            'id',
            'last_accessed_at',
        )
        fields = read_only_fields + (
            'username',
            'email',
            'password',
            'roles',
        )
        extra_kwargs = {'password': {'write_only': True}, 'password_recovery_code': {'write_only': True}}

    def get_roles(self, user):
        return [group.name for group in Group.objects.filter(user=user)]
