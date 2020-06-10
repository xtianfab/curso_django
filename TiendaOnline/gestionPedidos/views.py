from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.core.mail import send_mail# Create your views here.
from django.conf import settings

def form_contacto(request):

    if request.method =="POST":

        subject=request.POST["asunto"]
        message=request.POST["email"] + " " + request.POST["mensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["c.ram@hotmail.es"]
        send_mail(subject, message, email_from, recipient_list )
        return render(request, "gracias.html")

    return render(request, "contacto.html")
