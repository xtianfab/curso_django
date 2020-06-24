
# Relacion de uno a uno
# models.OneToOneField()

# Relacion de uno a muchos
# models.ForeignKey('self', on_delete=models.CASCADE).

# Relacion de muchos a muchos
# models.ManytuManyField()

from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)

class Foto(models.Model):
    #Relacionamos la foto con la clase Articulo
    #One to ONe Field
    articulo = models.OneToOneField("Articulo", on_delete=models.CASCADE)

    #One to many Field
    articulo = models.ForeignKey("Articulo", on_delete=models.CASCADE)

class Atributo(models.Model):

    nombre = models.CharField(max_length=150)
    #Relacionamos el atributo con la clase Articulo
    articulo = models.ManyToManyField("Articulo")


