# -*- coding: utf-8 -*-

from django.shortcuts import render
from carson.models import Products


def home(request):
    products = Products.objects.order_by('-published')[:4]
    data = {'data': products}
    return render(request, 'index.html', data)