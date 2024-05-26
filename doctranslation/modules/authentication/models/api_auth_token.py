from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token


class APIAuthToken(Token):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='api_auth_tokens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'API Auth Token'
