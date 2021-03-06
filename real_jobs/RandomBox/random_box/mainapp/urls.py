from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mainapp import views as mainapp

app_name="mainapp"

urlpatterns = [
    path("",mainapp.products, name="main"),
    path("<int:pk>/",mainapp.products, name="category"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
