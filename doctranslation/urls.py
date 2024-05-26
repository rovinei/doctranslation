from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('api/users/', include('doctranslation.modules.authentication.urls', namespace='users')),
    path('admin/', admin.site.urls),
]