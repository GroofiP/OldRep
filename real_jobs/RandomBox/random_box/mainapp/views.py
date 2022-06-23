import json
import os

from django.conf import settings
from django.shortcuts import render

from mainapp.models import Product, Product_Category


def index(request):
    context = {
        "title": "Random Box"
    }
    return render(request, "mainapp/index.html", context=context)


def products(request, pk=None):
    links = Product_Category.objects.all()
    products_all = Product.objects.all()
    if pk != None:
        products_all = Product.objects.filter(category__pk=pk)
    context = {
        "title": "Выбор бокса",
        "products": products_all,
        "links": links
    }
    return render(request, "mainapp/products.html", context=context)


def contacts(request):
    contacts_json = settings.BASE_DIR / "my_json/contacts.json"
    with open(contacts_json) as con_jon:
        locations = json.load(con_jon)

    context = {
        "title": "Контакты",
        "locations": locations
    }
    return render(request, "mainapp/contacts.html", context=context)
