from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

from .models import (
    Sala
    )
    
# Create your views here.
@login_required
def principal(request):

    return render(
        request,
        'principal.html'
    )

@login_required
def salas_estudo(request):
    # Olá #
    
    salas = Sala.objects.all().order_by('ordem', 'id')
    return render(
        request,
        'reservas/salas_estudo.html',
        {
            'salas': salas
        }
    )

@login_required
def lista_servidores(request):
    data={
        'servidores': User.objects.filter(is_staff=True),
    }
    
    return render(
        request,
        'servidores/lista_servidores.html',
        data
    )

@login_required
def set_delete_servidor(request, id_servidor):
    
    try:
        servidor = User.objects.get(id=id_servidor)
        servidor.delete()
    except:
        return redirect(reverse('lista_servidores') + '?message=Usuário não encontrado')
    
    return redirect('lista_servidores')