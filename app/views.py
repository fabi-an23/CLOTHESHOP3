from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForms, CustomUserCreationForms
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def home(request):
    return render(request, 'app/home.html')
@login_required
def contacto(request):
    data = {
        'form': ContactoForms()
    }

    if request.method =='POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def hombre(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/hombre.html', data)

def login(request):
    return render(request, 'app/login.html')

def mujer(request):
    return render(request, 'app/mujer.html')

def registro(request):
    data = {
        'form': CustomUserCreationForms()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            return redirect('home')  # Redirigir a la página "home" después de un registro exitoso
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)


def carrito(request):
    
    return render(request, 'app/carrito.html')



