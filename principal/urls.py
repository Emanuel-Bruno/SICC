from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import(
    principal,
    salas_estudo,
    lista_servidores,
    set_delete_servidor
)


urlpatterns = [
    path('', principal, name='principal'), # Pagina de boas vindas
    path('salas_estudo/', salas_estudo, name='salas_estudo'), # Hub das salas de estudo
    path('lista_servidores/', lista_servidores, name='lista_servidores'), # lista de servidores
    path('set_delete_servidor/<int:id_servidor>/', set_delete_servidor, name='set_delete_servidor')
]