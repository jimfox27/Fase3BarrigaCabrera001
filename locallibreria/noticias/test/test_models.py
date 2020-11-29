from django.test import TestCase
from noticias.models import User

# Create your tests here.
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(usuario='big', apellido='bob',nacimiento='2000-08-27',telefono='15151515',direccion='avpapaya123')
        
    def test_usuario_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('usuario').verbose_name
        self.assertEquals(field_label,'usuario')

    def test_nacimiento_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('nacimiento').verbose_name
        self.assertEquals(field_label,'Nacimiento')

    def test_usuario_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('usuario').max_length
        self.assertEquals(max_length,100)
    
    def test_object_name_is_apellido_comma_usuario(self):
        user=User.objects.get(id=1)
        expected_object_name = '%s, %s' % (user.usuario, user.apellido)
        self.assertEquals(expected_object_name,str(user))

    def test_get_absolute_url(self):
        user=User.objects.get(id=1)
        self.assertEquals(user.get_absolute_url(),'/user/1')