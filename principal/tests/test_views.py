import setup_django

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from ..models import Sala
from django.test import override_settings

from sistema_sicc.settings.base import TEST_SERVER, BASE_DIR
import os

### Classe de testes para as views
class ViewsTestCase(TestCase):

    ### Método que será executado antes de cada teste
    def setUp(self):
        ### Cria um cliente para realizar as requisições
        self.cliente = Client()

        ### Cria um usuário para realizar as requisições
        self.usuario = User.objects.create_user(username='usuarioTeste', password='Senha642', is_staff=True, is_superuser=True)

        ### Realiza o login do usuário
        self.client.login(username='usuarioTeste', password='Senha642')

        ### Cria uma sala para realizar os testes
        self.sala = Sala.objects.create(sala='Sala de Estudo', numero=10, estado='Disponível', ordem=1)
        self.url = TEST_SERVER


    ### Método para testar a view principal
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_principal_view(self):

        ### Realiza a requisição para a view principal
        response = self.client.get(reverse('principal'))

        ### Verifica se o status code da resposta é 200
        self.assertEqual(response.status_code, 200)

        ### Verifica se o template utilizado é o principal.html
        self.assertTemplateUsed(response, 'principal.html')

    ### Método para testar a view salas_estudo
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_salas_estudo_view(self):
        ### Realiza a requisição para a view salas_estudo
        response = self.client.get(reverse('salas_estudo'))

        ### Verifica se o status code da resposta é 200
        self.assertEqual(response.status_code, 200)
        

        ### Verifica se o template utilizado é o salas_estudo.html
        self.assertTemplateUsed(response, 'reservas/salas_estudo.html')
    
    ### Método para testar a view set_delete_sala
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_lista_servidores_view(self):

        ### Realiza a requisição para a view lista_servidores
        response = self.client.get(reverse('lista_servidores'))

        ### Verifica se o status code da resposta é 200
        self.assertEqual(response.status_code, 200)

        ### Verifica se o template utilizado é o lista_servidores.html
        self.assertTemplateUsed(response, 'servidores/lista_servidores.html')
    
    ### Método para testar a view set_delete_servidor
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_set_delete_servidor_view(self):

        ### Cria um servidor para realizar os testes
        servidor = User.objects.create_user(username='servidorTeste', password='Senha642', is_staff=True, is_superuser=True)
        
        ### Verifica se o usuário existe
        self.assertTrue(User.objects.filter(id=servidor.id).exists())

        ### Realiza a requisição para a view set_delete_servidor
        response = self.client.get(reverse('set_delete_servidor', args=[servidor.id]))

        ### Verifica se o status code da resposta é 302
        self.assertEqual(response.status_code, 302)

        ### Verifica se o usuário foi deletado
        self.assertRedirects(response, reverse('lista_servidores'))
        
        ### Verifica se o usuário foi deletado
        self.assertFalse(User.objects.filter(id=servidor.id).exists())

        ### Realiza a requisição para a view set_delete_servidor com usuário inexistente
        response = self.client.get(reverse('set_delete_servidor', args=[999]))

        ### Verifica se o status code da resposta é 302
        self.assertEqual(response.status_code, 302)

    
    ### Método para testar a view de adicionar usuário comum
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_set_post_user_view(self):
        ### Realiza a requisição para a view do admin para criar o usuário
        response = self.client.post(reverse('admin:auth_user_add'), data=({
            'username': 'servidorTeste',
            'password1': 'Senha642',
            'password2': 'Senha642',
        }))
        print(self.client)
        ### Verifica se o status code da resposta é 302
        self.assertEqual(response.status_code, 302)
        ### Verifica se o usuário existe
        self.assertTrue(User.objects.filter(username='servidorTeste').exists())

    
    ### Método para testar a view de adicionar usuário administrativo
    def test_set_user_admin_view(self):
        # Cria um superusuário diretamente
        User.objects.create_superuser(username='servidorTeste2', password='Senha642', email='')

        # Verifica se o usuário existe
        self.assertTrue(User.objects.filter(username='servidorTeste2').exists())

        # Verifica se o usuário é administrativo
        user = User.objects.get(username='servidorTeste2')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    ### Método para testar a view de adicionar usuário Servidor
    def test_set_user_servidor_view(self):
        # Cria um usuário servidor diretamente
        User.objects.create_user(username='servidorTeste2', password='Senha642', is_staff=True)

        # Verifica se o usuário existe
        self.assertTrue(User.objects.filter(username='servidorTeste2').exists())

        # Verifica se o usuário é staff
        user = User.objects.get(username='servidorTeste2')
        self.assertTrue(user.is_staff)

        




