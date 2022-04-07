from django.urls import URLPattern, path
from AppCommerce.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('adornos/', adornos, name="Adornos"),
    path('souvenirs/', souvenirs, name="Souvenirs"),
    path('pagos/', pagos, name="Pagos"),
]