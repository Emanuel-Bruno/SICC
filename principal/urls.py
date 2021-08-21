from django.urls import path
from .views import(
    principal,
    salas_estudo,
)

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', principal, name='principal'),
    path('salas_estudo/', salas_estudo, name='salas_estudo')
]