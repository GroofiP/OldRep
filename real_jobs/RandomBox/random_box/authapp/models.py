from django.contrib.auth.models import AbstractUser
from django.db import models


class Shop_User(AbstractUser):
    avatar = models.ImageField(upload_to="users_avatars", blank=True, verbose_name="Аватар")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
