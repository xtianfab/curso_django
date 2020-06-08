# 1. Crear un archivo "vista", por convencion se crea con el nombre views.py

# 2. Dentro del archivo creamos una funcion en donde pasaremos como parametro la peticion. 
#   - El nombre de la funcion puede ser cualquiera
#   - La funcion retorna un HttpResponse
#   - Debemos importar el desde el modulo django.http

# from django.http import HttpResponse

# def saludo(request):
#     return HttpResponse("Hola Cristian")

# 3. En el archivo urls.py debemos declarar la funcion creada.
#     - El nombre del path puede ser cualquiera
#     - En urls.py debemos importar la funcion desde el archivo views.py

# #from Proyecto1.views import saludo

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('saludo/', saludo)
# ]

# 4.  Pasar varios parametros a la url
# 4.1 En nuestra funcion definimos el parametro o parametros a pasar

# def variosParametros(request, param1, param2):
#     param1 =""
#     param2 =""
#     return HttpResponse(f"Hola Cristian {param1} {param2}")

# 4.2 Debemos declarar en el archivo url el o los parametros dentro de corchetes angulares "<>"
#     - En caso de pasar paramtros numericos debemos convertirlos a enteros int:param1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('saludo/', saludo)
#     path('pasaParametros/<int:param1>/<param2>', variosParametros)
# ]
