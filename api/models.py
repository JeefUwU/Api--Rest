from django.db import models

# Create your models here.


class Producto(models.Model):
    codigo_producto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    codigo = models.CharField(max_length= 100)
    nombre = models.CharField (max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre