
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication

from doctranslation.modules.authentication.models import APIAuthToken


class APITokenAuthentication(TokenAuthentication):
    keyword = 'doctranslation'
    model = APIAuthToken
