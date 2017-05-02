# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Provincia(models.Model):
    code=models.CharField(max_length=2)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Canton(models.Model):
    code=models.CharField(max_length=2)
    name=models.CharField(max_length=200)
    provincia=models.ForeignKey(Provincia)
    def __str__(self):
        return self.name
class Parroquia(models.Model):
    code=models.CharField(max_length=2)
    name=models.CharField(max_length=200)
    parroquia=models.ForeignKey(Canton)
    def __str__(self):
        return self.name
class Uso(models.Model):
    code=models.CharField(max_length=2)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Fuente(models.Model):
    code=models.CharField(max_length=2)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Unidad(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Concesion(models.Model):
    latitud=models.CharField(max_length=15)
    longitud=models.CharField(max_length=15)
    altura=models.IntegerField
    parroquia=models.ForeignKey(Parroquia)
    uso=models.ForeignKey(Uso)
    fuente=models.ForeignKey(Fuente)
    unidad=models.ForeignKey(Unidad)
    concesionario=models.TextField
    proceso=models.IntegerField
    caudal_med=models.DecimalField
    caudal_con=models.DecimalField
    actualizacion=models.IntegerField
