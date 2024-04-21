from django.db import models
from django.urls import reverse
from django.utils.html import format_html

class Sala(models.Model):
    
    ESTADO = (
        ('Disponível', 'Disponível'),
        ('Ocupado', 'Ocupado'),
        ('Indisponível', 'Indisponível'),
    )

    sala = models.CharField(
        verbose_name="Nome",
        max_length=30,
        null=True, blank=False
    )

    numero = models.IntegerField(
        verbose_name="Número",
        null=True, blank=False
    )

    estado = models.CharField(
        choices=ESTADO,
        max_length=30,
        verbose_name="Estado",
        default=('Disponível', 'Disponível'),
        null=True, blank=False
    )

    ordem = models.IntegerField(
        verbose_name="Ordem",
        default=99,
        null=True, blank=False
    )

    @property
    def reservar(self):
        if self.estado == 'Disponível':
            url = reverse('admin:principal_reserva_add')  # substitua 'app' pelo nome do seu aplicativo
            params = '?sala=' + str(self.id)
            return format_html('<a class="btn btn-primary" href="{}">Reservar</a>', url + params)
        else:
            return format_html('<span class="btn btn-danger">Opção indisponível</span>')

    def desocupar(self):
        self.estado = 'Disponível'
        self.save()

    def indisponibilizar(self):
        self.estado = 'Indisponível'
        self.save()

    def __str__(self):
        return "{} Nº{}".format(self.sala, self.numero)