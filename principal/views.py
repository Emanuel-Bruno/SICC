from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        'servidores': User.objects.filter(is_staff=True)
    }
    
    return render(
        request,
        'servidores/lista_servidores.html',
        data
    )

@login_required
def dashboard(request):
    
    return render(
        request,
        'dashboard/dashboard.html'
    )

@login_required
def relatorio_salas(request):
    
    return render(
        request,
        'relatorio/relatorio_salas.html'
    )

@login_required
def form_relatorio(request):
    
    return render(
        request,
        'relatorio/form_relatorio.html'
    )
@login_required
def form_dashboard(request):
    
    return render(
        request,
        'dashboard/form_dashboard.html'
    )

@login_required
def get_status_sala(request):

    salas = Sala.objects.all()
    data_response={

    }
    return JsonResponse(data=data_response, safe=False)


@login_required
def set_delete_servidor(request, id_servidor):
    servidor = User.objects.get(id=id_servidor)
    servidor.delete()

    return redirect('lista_servidores')