# -*- coding: utf-8 -*-

from django.shortcuts import render
from carson.models import Products, Slides


def home(request):
    products = Products.objects.order_by('-published')[:4]
    slides = Slides.objects.filter(active=True)
    data = {'data': products, 'slides': slides}
    return render(request, 'index.html', data)


def product(request, id):
    product = Products.objects.get(id=id)
    data = {'product': product}
    return render(request, 'product.html', data)