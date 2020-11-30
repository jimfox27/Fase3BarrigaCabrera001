from django.test import TestCase, Client
from django.urls import reverse
from noticias.models import Post, Analisis, Foro

class Testviews(TestCase):

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('agregar_noticia'))

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'crud_noticia/agregar.html')