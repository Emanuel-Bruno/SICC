from django.test import TestCase
from principal.forms import ReservaForm
from django.contrib.auth.models import User
from principal.models import Sala, Reserva
from datetime import datetime, timedelta
from django.utils import timezone

### Testando ReservaForm
class ReservaFormTest(TestCase):
    ### Configuração do teste
    def setUp(self):
        self.usuario = User.objects.create_user(username='usuarioTeste', password='Senha642', is_staff=False, is_superuser=False)
        self.sala = Sala.objects.create(sala='Sala de Estudo', numero=10, estado='Disponível', ordem=1)
        self.sala2 = Sala.objects.create(sala='Sala de Estudo 20', numero=20, estado='Disponível', ordem=1)
        data_inicial=datetime.now()
        data_final=datetime.now()+timedelta(hours=1)
        self.data_inicial_aware = timezone.make_aware(data_inicial)
        self.data_final_aware = timezone.make_aware(data_final)

    ### Teste de formulário válido
    def test_reserva_form_valid_data(self):

        form = ReservaForm(data={
            'responsavel': self.usuario,
            'sala': self.sala2,
            'data_inicial': self.data_inicial_aware,
            'data_final': self.data_final_aware
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    ### Teste de atualização de valor
    def test_reserva_form_change_valid_data(self):
        reserva = Reserva.objects.create(
            responsavel=self.usuario,
            sala=self.sala,
            data_inicial=self.data_inicial_aware,
            data_final=self.data_final_aware
        )
        form = ReservaForm(data={
            'responsavel': self.usuario,
            'sala': self.sala,
            'data_inicial': self.data_inicial_aware,
            'data_final': self.data_final_aware
        }, instance=reserva)
        self.assertTrue(form.is_valid())

    ### Teste de formulário inválido
    def test_reserva_form_invalid_data(self):
        form = ReservaForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
