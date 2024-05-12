from django.db import models

# Create your models here.


class Producto(models.Model):
    codigo_producto = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    codigo = models.CharField(max_length= 10)
    nombre = models.CharField (max_length=50)
    precio = models.PositiveBigIntegerField()
    fecha = models.DateField()