from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "telf")
    search_fields=("nombre", "direccion", "email", "telf")
    list_filter=("nombre", "direccion","telf")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    search_fields=("nombre", "seccion", "precio")
    list_filter=("nombre", "seccion", "precio")

class PedidosAdmin(admin.ModelAdmin):
    list_display=("nro_pedido", "fecha", "entregado")
    search_fields=("nro_pedido", "fecha", "entregado")
    list_filter=("nro_pedido", "fecha", "entregado")
    date_hierarchy="fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)