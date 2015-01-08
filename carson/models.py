# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Category, related_name='sub')

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

    def __unicode__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Product title')
    description = models.TextField()
    photo = models.FileField(upload_to='images/products/')
    published = models.DateField(verbose_name='Date')
    category = models.ForeignKey(SubCategory, default=None, blank=True, null=True)

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


class ImgBlocks(models.Model):
    name = models.CharField(max_length=255, verbose_name='Block name')
    image = models.FileField(upload_to='images/blocks/', help_text='320x160')
    description = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Products)
    published = models.DateField(verbose_name='Date')

    class Meta:
        verbose_name_plural = 'Homepage image-blocks'

    def __unicode__(self):
        return self.name
