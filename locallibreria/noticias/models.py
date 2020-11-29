from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from locallibreria.utils import unique_slug_generator_foro, unique_slug_generator_noticia, unique_slug_generator_analisis
import uuid
from ckeditor.fields import RichTextField

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    nombrejuego = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    slug = models.SlugField('Slug', max_length = 200, null=True, blank=True)    
    genero = models.ManyToManyField(Genero)
    contenido = RichTextField()
    imagen = models.ImageField(null = True, upload_to="post")
    fecha_publicacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    def __str__(self):
        return self.titulo

class Analisis(models.Model):
    nombrejuego = models.CharField(max_length=200)
    slug = models.SlugField('Slug', max_length = 200, null=True, blank=True)
    genero = models.ManyToManyField(Genero)
    contenido = RichTextField()
    puntuacion = models.CharField('Nota del juego (0.1, 1.0)', max_length=3)
    imagen = models.ImageField(null = True, upload_to="analisis")
    fecha_publicacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    def __str__(self):
        return self.nombrejuego


class Foro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foros', default='1')
    tema = models.CharField(max_length=200)
    slug = models.SlugField('Slug', max_length = 200, null=True, blank=True)
    contenido = RichTextField()
    fecha_publicacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    def __str__(self):
        return self.tema


def slug_generator_noticia(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_noticia(instance)
def slug_generator_analisis(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_analisis(instance)
def slug_generator_foro(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_foro(instance)

pre_save.connect(slug_generator_noticia, sender=Post)
pre_save.connect(slug_generator_analisis, sender=Analisis)
pre_save.connect(slug_generator_foro, sender=Foro)

def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

post_save.connect(crear_perfil, sender=User)

class Comentario(models.Model):
    post = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name='comentario', default='1')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nombre', default='1')
    body = models.TextField()
    fecha_publicacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    ordering = ['fecha_publicacion']

    def __str__(self):
        return self.tema