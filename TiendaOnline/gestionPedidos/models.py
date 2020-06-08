from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    telf= models.CharField(max_length=10, verbose_name="Telefono")

    # def __str__(self):
    #     return f"{self.nombre}, {self.direccion}, {self.email}, {self.telf}"

class Articulos(models.Model):
    nombre = models.CharField(max_length=20)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    # def __str__(self):
    #     return f"{self.nombre}, {self.seccion}, {self.precio}"

class Pedidos(models.Model):
    nro_pedido = models.IntegerField(verbose_name="Nro. de Pedido")
    fecha = models.DateField()
    entregado = models.BooleanField(verbose_name="Entregado?")



