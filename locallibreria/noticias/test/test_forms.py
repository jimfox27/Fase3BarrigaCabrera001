from django.test import SimpleTestCase
from noticias.forms import ForoForm

class TestForm(SimpleTestCase):
    
    def test_foro_form_valid_data(self):
        form = ForoForm(data={
            'tema': 'Supermariokong',
            'contenido': 'Super mario saca un nuevo juego'
        })
        self.assertTrue(form.is_valid())