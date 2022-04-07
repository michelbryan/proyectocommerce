from mailbox import NoSuchMailboxError
from django.shortcuts import render
from AppCommerce.models import Adornos, Pago, Souvenir

# Create your views here.

def adornos(request):
    adorno = Adornos.objects.all()
    return render(request, "AppCommerce/adornos.html", {"adornos": adorno})

def souvenirs(request):
    souvenir = Souvenir.objects.all()
    return render(request, "AppCommerce/souvenirs.html", {"souvenirs": souvenir})

def pagos(request):
    pago = Pago.objects.all()
    return render(request, "AppCommerce/pagos.html", {"pagos": pago})

def inicio(request):
    return render(request, "AppCommerce/index.html")

    