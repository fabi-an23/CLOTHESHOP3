from django.urls import path
from .views import home, contacto, hombre, login, mujer, registro, carrito

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('hombre/', hombre, name="hombre"),
    path('login/', login, name="login"),
    path('mujer/', mujer, name="mujer"),
    path('registro/', registro, name="registro"),
    path('carrito/', carrito, name="carrito"),
]