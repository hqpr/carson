# -*- coding: utf-8 -*-
from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Product title')
    description = models.TextField()
    photo = models.FileField(upload_to='images/products/')
    published = models.DateField(verbose_name='Date')

    class Meta:
        verbose_name = 'Product'

    def __unicode__(self):
        return u'%s' % self.title


class Slides(models.Model):
    name = models.CharField(max_length=255, verbose_name='Slide name')
    image = models.FileField(upload_to='images/slider/')
    active = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Slides'
        verbose_name_plural = 'Slides'

    def __unicode__(self):
        return self.name