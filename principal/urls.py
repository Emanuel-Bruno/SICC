from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import(
    principal,
    salas_estudo,
    lista_servidores,
    relatorio_salas,
    dashboard,
    form_dashboard,
    form_relatorio
)


urlpatterns = [
    path('', principal, name='principal'), # Pagina de boas vindas
    path('salas_estudo/', salas_estudo, name='salas_estudo'), # Hub das salas de estudo
    path('lista_servidores/', lista_servidores, name='lista_servidores'), # lista de servidores
    path('relatorio_salas/', relatorio_salas, name='relatorio_salas'), # Relatorio das reservas
    path('dashboard/', dashboard, name='dashboard'), # dashboard
    path('form_dashboard/', form_dashboard, name='form_dashboard'), # form_dashboard
    path('form_relatorio/', form_relatorio, name='form_relatorio'), # form_relatorio
]