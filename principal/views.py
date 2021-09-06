from django.shortcuts import render
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