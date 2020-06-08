from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telf= models.CharField(max_length=10)

class Articulos(models.Model):
    nombre = models.CharField(max_length=20)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    nro_pedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()



