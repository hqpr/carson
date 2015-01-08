# -*- coding: utf-8 -*-

from django.shortcuts import render
from carson.models import Products, Slides, ImgBlocks, Category, SubCategory


def home(request):
    products = Products.objects.order_by('-published')[:4]
    slides = Slides.objects.filter(active=True)
    imgblocks = ImgBlocks.objects.order_by('-published')[:3]
    categories = Category.objects.all()
    data = {'data': products, 'slides': slides, 'imgblocks': imgblocks, 'categories': categories}
    return render(request, 'index.html', data)


def product(request, id):
    product = Products.objects.get(id=id)
    data = {'product': product}
    return render(request, 'product.html', data)