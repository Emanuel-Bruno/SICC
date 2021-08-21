from django.db import models

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

    def __str__(self):
        return "{} Nº{}".format(self.sala, self.numero)