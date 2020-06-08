#Para crear un proyecto nuevo debemos escribir el siguiente comando desde cmd

# django-admin startproject Proyecto1

# Creara 1 carpeta con el nombre indicado

# -Proyecto1
#     --Proyecto1
#         ---__init__.py    --> Archivo necesrio, indica que la carpeta es un paquete
#         ---asgi.py
#         ---settings.py    --> Contiene todas las configuraciones de nuestro proyecto
#         ---urls.py        --> Donde se almacenan las urls de nuestro proyecto, como un indice
#         ---wsgi.py        --> Es relativo al servidor web
#     --mamage.py           --> manage.py help


#Activar el proyecto
#python manage.py migrate  --> Este comando creara la base de datos dentro de la carpeta


#Correr servidor
#python manage.py runsever