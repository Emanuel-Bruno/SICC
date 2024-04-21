from django import forms
from ..models import Reserva, Sala
from django.db.models import Q

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['sala'].queryset = Sala.objects.filter(Q(estado='Disponível') | Q(id=self.instance.sala.id))
        else:
            self.fields['sala'].queryset = Sala.objects.filter(estado='Disponível')