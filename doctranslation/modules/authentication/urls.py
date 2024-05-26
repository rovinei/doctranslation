from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    SignInView,
    SignOutView,
    SignUpView,
    UserViewSet,
)

app_name = 'user'

router = routers.SimpleRouter()
router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('', include(router.urls)),
]
