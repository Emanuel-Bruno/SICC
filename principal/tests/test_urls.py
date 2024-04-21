import setup_django
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from principal.views import (
    principal,
    salas_estudo,
    lista_servidores,
    set_delete_servidor
)

### TESTANDO URLS
class TestUrls(SimpleTestCase):

    ### Página inicial
    def test_principal_url(self):
        url = reverse('principal')
        self.assertEqual(resolve(url).func, principal)

    ### Lista das salas de estudo
    def test_salas_estudo_url(self):
        url = reverse('salas_estudo')
        self.assertEqual(resolve(url).func, salas_estudo)

    ### Lista de servidores
    def test_lista_servidores_url(self):
        url = reverse('lista_servidores')
        self.assertEqual(resolve(url).func, lista_servidores)

    ### Remoção de servidor
    def test_set_delete_servidor_url(self):
        url = reverse('set_delete_servidor', args=[1])
        self.assertEqual(resolve(url).func, set_delete_servidor)