from django.contrib import admin
from .models import Sala

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
	list_display = ('id', 'sala', 'numero', 'estado')