import json
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from authapp.models import Shop_User
from mainapp.models import Product_Category, Product

JSON_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')

def load_json_data(file_name):
    with open(os.path.join(JSON_PATH, file_name + ".json")) as json_file:
        return json.load(json_file)



class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        categories = load_json_data("categories")
        Product_Category.objects.all().delete()
        for category in categories:
            Product_Category.objects.create(**category)

        products = load_json_data("products")
        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            _category = Product_Category.objects.get(name=category_name)
            product["category"] = _category
            Product.objects.create(**product)

        Shop_User.objects.create_superuser('django', 'django@geekbrains.local', 'geekbrains', age=33)
