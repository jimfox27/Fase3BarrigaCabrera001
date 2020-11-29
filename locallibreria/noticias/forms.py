from django import forms
from .models import  Post, Analisis, Foro, Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

class AnalisisForm(forms.ModelForm):

    class Meta:
        model = Analisis
        fields = '__all__'

class ForoForm(forms.ModelForm):
    tema = forms.CharField()
    contenido = forms.CharField()
    
    class Meta:
        model = Foro
        fields = ['tema','contenido']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = '__all__'