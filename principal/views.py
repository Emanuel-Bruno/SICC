from django.shortcuts import render
from .models import (
    Sala
    )
# Create your views here.

def principal(request):

    return render(
        request,
        'principal.html'
    )

def salas_estudo(request):
    # Olá #
    
    salas = Sala.objects.all()
    return render(
        request,
        'salas_estudo.html',
        {
            'salas': salas
        }
    )