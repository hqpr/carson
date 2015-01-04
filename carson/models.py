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