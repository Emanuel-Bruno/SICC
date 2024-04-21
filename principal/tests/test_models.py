import setup_django
from django.test import TestCase
from principal.models import Sala, Reserva
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import Group, Permission
from django.urls import reverse
from django.utils.html import format_html
### Teste do modelo Sala
class SalaTestCase(TestCase):

    ### Configuração do teste
    def setUp(self):
        self.sala = Sala.objects.create(sala='Sala de Estudo', numero=10, estado='Disponível', ordem=1)
        self.usuario = User.objects.create_user(username='usuarioTeste', password='Senha642', is_staff=False, is_superuser=False)
    ### Teste de criação do modelo
    def test_model_creation(self):
        self.assertIsInstance(self.sala, Sala)

    ### Teste de atributos do modelo
    def test_model_attributes(self):
        self.assertEqual(self.sala.sala, "Sala de Estudo")
        self.assertEqual(self.sala.numero, 10)
        self.assertEqual(self.sala.estado, "Disponível")
        self.assertEqual(self.sala.ordem, 1)
    
    def test_model_methods(self):
        self.assertEqual(self.sala.estado, "Disponível")
        data_inicial=datetime.now()
        data_final=datetime.now()+timedelta(hours=1)
        data_inicial_aware = timezone.make_aware(data_inicial)
        data_final_aware = timezone.make_aware(data_final)
        Reserva.objects.create(sala=self.sala, responsavel=self.usuario, data_inicial=data_inicial_aware, data_final=data_final_aware)
        
        ### Teste de ocupação de sala
        self.assertEqual(self.sala.estado, "Ocupado")

        ### Teste de desocupação de sala
        self.sala.desocupar()
        self.assertEqual(self.sala.estado, "Disponível")

        ### Teste de sala indisponível
        self.sala.indisponibilizar()
        self.assertEqual(self.sala.estado, "Indisponível")
        code_html = format_html('<span class="btn btn-danger">Opção indisponível</span>')
        self.assertHTMLEqual(self.sala.reservar, code_html)

        ### Teste de sala disponível
        self.sala.desocupar()
        self.assertEqual(self.sala.estado, "Disponível")
        
        url = reverse('admin:principal_reserva_add')  # substitua 'app' pelo nome do seu aplicativo
        params = '?sala=' + str(self.sala.id)
        code_html = format_html('<a class="btn btn-primary" href="{}">Reservar</a>', url + params)
        self.assertHTMLEqual(self.sala.reservar, code_html)

        

### Teste do modelo Reserva
class ReservaTestCase(TestCase):

    ### Configuração do teste
    def setUp(self):
        self.sala = Sala.objects.create(sala='Sala de Estudo', numero=10, estado='Disponível', ordem=1)
        self.usuario = User.objects.create_user(username='usuarioTeste', password='Senha642', is_staff=False, is_superuser=False)
        data_inicial=datetime.now()
        data_final=datetime.now()+timedelta(hours=1)
        self.data_inicial_aware = timezone.make_aware(data_inicial)
        self.data_final_aware = timezone.make_aware(data_final)
        self.reserva = Reserva.objects.create(sala=self.sala, responsavel=self.usuario, data_inicial=self.data_inicial_aware, data_final=self.data_final_aware)

    ### Teste de criação do modelo
    def test_model_creation(self):
        self.assertIsInstance(self.reserva, Reserva)

    ### Teste de atributos do modelo
    def test_model_attributes(self):
        self.assertEqual(self.reserva.sala, self.sala)
        self.assertEqual(self.reserva.responsavel, self.usuario)
        self.assertEqual(self.reserva.data_inicial, self.data_inicial_aware)
        self.assertEqual(self.reserva.data_final, self.data_final_aware)
    ### Teste de métodos do modelo
    def test_model_methods(self):
        ### Teste do metodo str
        self.assertEqual(self.reserva.__str__(), str(self.reserva.id))
    


### Teste do modelo User
class UserTestCase(TestCase):

    ### Configuração do teste
    def setUp(self):
        ### Cria um usuário para realizar os testes
        self.usuario = User.objects.create_user(
            username='usuarioTeste', 
            password='Senha642', 
            is_staff=False, 
            is_superuser=False,
            email='emanuelbruno2018vasc@gmail.com',
            first_name='Emanuel',
            last_name='Morais'
        )
    ### Teste de criação do modelo
    def test_model_creation(self):
        ### Verifica se o modelo foi criado
        self.assertIsInstance(self.usuario, User)
    
    ### Teste de atributos do modelo
    def test_model_attributes(self):
        ### Verifica se os atributos foram criados corretamente
        self.assertEqual(self.usuario.username, "usuarioTeste")
        self.assertFalse(self.usuario.is_staff)
        self.assertFalse(self.usuario.is_superuser)
        self.assertEqual(self.usuario.email, "emanuelbruno2018vasc@gmail.com")
        self.assertNotEqual(self.usuario.email, "emailERRADO@gmail.com")
        self.assertTrue(self.usuario.is_active)

    ### Teste de métodos do modelo
    def test_model_methods(self):
        ### Verifica se os métodos do modelo estão funcionando corretamente
        self.assertEqual(self.usuario.get_full_name(), "Emanuel Morais")
        self.assertEqual(self.usuario.get_short_name(), "Emanuel")
        self.assertFalse(self.usuario.has_perm('perm'))
        self.assertFalse(self.usuario.has_module_perms('module'))
        self.assertEqual(self.usuario.get_username(), "usuarioTeste")
        self.assertEqual(self.usuario.get_user_permissions(), set())
        self.assertEqual(self.usuario.get_group_permissions(), set())
        self.assertEqual(self.usuario.get_all_permissions(), set())
        self.assertEqual(self.usuario.groups.count(), 0)
        self.assertEqual(self.usuario.user_permissions.count(), 0)
        
### Teste do modelo Group
class GroupTestCase(TestCase):
    
        ### Configuração do teste
        def setUp(self):
            ### Cria um grupo para realizar os testes
            self.grupo = Group.objects.create(name='GrupoTeste')
    
        ### Teste de criação do modelo
        def test_model_creation(self):
            ### Verifica se o modelo foi criado
            self.assertIsInstance(self.grupo, Group)
        
        ### Teste de atributos do modelo
        def test_model_attributes(self):
            ### Verifica se os atributos foram criados corretamente
            self.assertEqual(self.grupo.name, "GrupoTeste")
        
        ### Teste de métodos do modelo
        def test_model_methods(self):
            ### Verifica se os métodos do modelo estão funcionando corretamente
            self.assertEqual(self.grupo.permissions.count(), 0)
            self.assertEqual(self.grupo.user_set.count(), 0)
            self.assertEqual(self.grupo.permissions.count(), 0)