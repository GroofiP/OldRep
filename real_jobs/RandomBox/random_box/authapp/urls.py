from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from authapp import views as authapp

app_name="authapp"

urlpatterns = [
    path("login/",authapp.login, name="login"),
    path("logout/",authapp.logout, name="logout"),
    path("register/",authapp.register, name="register"),
    path("edit/",authapp.edit, name="edit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

