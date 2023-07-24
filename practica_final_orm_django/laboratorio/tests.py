from django.test import TestCase
from django.test import SimpleTestCase  # para el testo de paginas estaticas
from django.urls import reverse

from .models import Laboratorio

# Create your tests here.


class LaboratorioTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio 2', ciudad='Ciudad 2', pais='País 2')

    def test_contenido_laboratorio(self):
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio 2')
        self.assertEqual(self.laboratorio.ciudad, 'Ciudad 2')
        self.assertEqual(self.laboratorio.pais, 'País 2')


class UrlsTest(SimpleTestCase):
    def test_url_existe(self):
        response = self.client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)

    def test_url_por_nombre(self):
        response = self.client.get(reverse('laboratorio'))
        self.assertEqual(response.status_code, 200)

    def test_nombre_plantilla_correcto(self):
        response = self.client.get(reverse('laboratorio'))
        self.assertTemplateUsed(response, 'laboratorio/laboratorio.html')

    def test_contenido(self):
        response = self.client.get(reverse('laboratorio'))
        self.assertContains(response, '<p>Esto es un test</p>')
        self.assertNotContains(response, 'No es la pagina')
