from django.urls import path

from staticapp.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
