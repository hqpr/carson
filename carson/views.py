# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Products, Slides, ImgBlocks, Category, SubCategory


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
    
    
def create_superuser(request):
    User.objects.create_user('admin', 'adubnyak@gmail.com', 1)
    return None
