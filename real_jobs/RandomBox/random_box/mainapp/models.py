from django.db import models


class Product_Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Имя")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=128, verbose_name="Название")
    image = models.ImageField(upload_to="products_images", blank=True, verbose_name="Картинка")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    is_active = models.BooleanField(default=True, verbose_name="активна")

    def __str__(self):
        return f" {self.name} ({self.category.name})"
