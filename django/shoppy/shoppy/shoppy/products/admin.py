# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
from .models import Favorite
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=('id','name','category','description','price')
    list_filter=('category',)
@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display=('user','product')
    list_filter=('user','product',)
