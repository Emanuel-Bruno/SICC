from django.db import models
from .sala import Sala

class Reserva(models.Model):
    sala = models.OneToOneField(
        Sala,
        verbose_name='Sala',
        on_delete=models.CASCADE,
    )

    responsavel = models.ForeignKey(
		'auth.User',
        verbose_name="Responsável",
		blank=True, null=True,
		on_delete=models.SET_NULL
	)

    data_inicial = models.DateTimeField(
        verbose_name='Inicio'
    )

    data_final = models.DateTimeField(
        verbose_name='Final'
    )

    def __str__(self):
        return "{}".format(self.id)