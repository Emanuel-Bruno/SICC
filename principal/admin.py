from django.contrib import admin
from .models import Sala
from .models import Reserva


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
	list_display = ('id', 'sala', 'numero', 'estado')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	list_display = ('id', 'sala')