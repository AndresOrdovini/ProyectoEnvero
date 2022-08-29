from django.db import models

# Create your models here.

class inicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class problema(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class solucion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class caracteristicas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class mercado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()

class equipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.IntegerField()