from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Message(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Введите сообщение")

    def __str__(self):
        return f"{self.name}: {self.text}"
