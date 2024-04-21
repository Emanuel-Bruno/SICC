from django.contrib import admin
from .models import Sala
from .models import Reserva
from django_object_actions import DjangoObjectActions
from .forms import ReservaForm
from django.shortcuts import redirect
from django.urls import reverse


@admin.register(Sala)
class SalaAdmin(DjangoObjectActions, admin.ModelAdmin):
	list_display = ('id', 'sala', 'numero', 'estado')
	list_filter = ('estado',)
	change_actions = ['desocupar','indisponibilizar']

	readonly_fields = ('estado', 'reservar')

     
	def desocupar(self, request, obj):
		obj.desocupar()

	desocupar.label = 'Desocupar/Disponibilizar'
	desocupar.short_description = 'Esta ação vai desocupar a sala e torná-la disponível.'

	def indisponibilizar(self, request, obj):
		obj.indisponibilizar()

	indisponibilizar.label = 'Indisponibilizar'
	indisponibilizar.short_description = 'Esta ação vai indisponibilizar a sala.'

	def get_change_actions(self, request, object_id, form_url):
		actions = []
		obj = self.get_object(request, object_id)
		if obj.estado == 'Ocupado' or obj.estado == 'Indisponível':
			actions.append('desocupar')
		if obj.estado == 'Disponível' or obj.estado == 'Ocupado':
			actions.append('indisponibilizar')

		return actions


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	list_display = ('id', 'sala')
	form = ReservaForm
	