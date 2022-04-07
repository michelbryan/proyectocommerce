from pickle import TRUE
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class Adornos(models.Model):
    
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField(primary_key=True)


class Souvenir(models.Model):
    
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField(primary_key=True)

class Pago(models.Model):
    
    nombre = models.CharField(max_length=15)
    numero_cliente = models.IntegerField(primary_key=True)
    importe = models.IntegerField()
    fecha_pago = models.DateField()
