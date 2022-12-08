from django.db import models

# Create your models here.
#creando un abstract
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    peso = models.CharField(max_length=50)

    class Meta:
        abstract = True

#herencia de clase
class Refri(Producto):
    min_temperatura = models.CharField(max_length=50)
    smart_screen = models.CharField(max_length=50)
    volumen = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

class Laptop(Producto):
    modelo_cpu = models.CharField(max_length=50)