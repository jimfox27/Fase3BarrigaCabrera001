from .models import *
from django.core.paginator import Paginator
from .models import Post, Analisis, User, Foro, Comentario
from django.contrib.auth.models import User
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .forms import PostForm
from .forms import AnalisisForm
from .forms import ForoForm
from .forms import ComentarioForm

# Create your views here.
def index(request):

    num_noticias=Post.objects.all().count()
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    postsAnalisis = Analisis.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    #paginacion
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    paginator = Paginator(postsAnalisis,5)
    pageAnalisis = request.GET.get('page')
    postsAnalisis = paginator.get_page(page)

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'index.html',{'num_noticias':num_noticias,'posts': posts, 'postsAnalisis': postsAnalisis})

def analisisPost(request,slug):
    num_noticias=Post.objects.all().count()
    posts = Analisis.objects.filter()

    post = Analisis.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'juego.html',{'analisis_post':post, 'posts': posts, 'num_noticias':num_noticias})

def foroPost(request,slug):
    num_noticias=Post.objects.all().count()
    posts = Foro.objects.filter()

    post = Foro.objects.get(
        slug = slug
    )

    print(post)
    return render(request,'discusion.html',{'foro_post':post, 'posts': posts, 'num_noticias':num_noticias})

def detallePost(request,slug):
    num_noticias=Post.objects.all().count()
    posts = Post.objects.filter()

    post = Post.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'reportaje.html',{'detalle_post':post, 'num_noticias':num_noticias,'posts': posts})

def noticias(request):
    num_noticias=Post.objects.all().count()
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    ultimaNoticia = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    paginator = Paginator(ultimaNoticia,1)
    page = request.GET.get('page')
    ultimaNoticia = paginator.get_page(page)

    return render(request,'noticias.html',{'num_noticias':num_noticias,'posts': posts, "ultimaNoticia": ultimaNoticia,})
    
def analisis(request):

    num_noticias=Post.objects.all().count()
    postsAnalisis = Analisis.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    ultimoAnalisis = Analisis.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    paginator = Paginator(postsAnalisis,10)
    pageAnalisis = request.GET.get('page')
    postsAnalisis = paginator.get_page(pageAnalisis)

    paginator = Paginator(ultimoAnalisis,1)
    page = request.GET.get('page')
    ultimoAnalisis = paginator.get_page(page)

    return render(request,'analisis.html',{'num_noticias':num_noticias, 'postsAnalisis': postsAnalisis, 'ultimoAnalisis': ultimoAnalisis,})

def foro(request):

    queruset = request.GET.get("buscar")
    num_noticias = Post.objects.all().count()
    ultimoForo = Foro.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    
    if queruset:
        ultimoForo = Foro.objects.filter(
            Q(tema__icontains = queruset)
        ).distinct()

    paginator = Paginator(ultimoForo,10)
    page = request.GET.get('page')
    ultimoForo = paginator.get_page(page)

    return render(request,'foro.html',{'num_noticias':num_noticias, 'ultimoForo': ultimoForo,})

# CRUD #
def agregar_noticia(request):

    data = {
        'form': PostForm()
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Con Exito"
        else:
            data["form"] = formulario

    return render(request, 'crud_noticia/agregar.html', data)

def modificar_noticia(request, slug):
    post = get_object_or_404(Post, slug=slug)

    data = {
        'form': PostForm(instance=post)
    }

    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=post, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "modificado correctamente"
            return redirect(to="noticias")

    return render(request, 'crud_noticia/modificar.html', data)

def listar_noticia(request):
    queruset = request.GET.get("buscar")
    post = Post.objects.all()

    if queruset:
        post = Post.objects.filter(
            Q(titulo__icontains = queruset)
        ).distinct()
    
    paginator = Paginator(post,10)
    page = request.GET.get('page')
    post = paginator.get_page(page)

    data = {
        'post': post
    }
    return render(request, 'crud_noticia/listar.html', data)

def eliminar_noticia(request, slug):

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(to="listar_noticia")

## CRUD ANALISIS##
def agregar_analisis(request):

    data = {
        'form': AnalisisForm()
    }

    if request.method == 'POST':
        formulario = AnalisisForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            data["mensaje"] = "Guardado Con Exito"
        else:
            data["mensaje"] = "Guardado Con Exito"
            data["form"] = formulario

    return render(request,  'crud_analisis/agregar.html', data)

def modificar_analisis(request, slug):
    analisis = get_object_or_404(Analisis, slug=slug)

    data = {
        'form': AnalisisForm(instance=analisis)
    }

    if request.method == 'POST':
        formulario = AnalisisForm(data=request.POST, instance=analisis, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "modificado correctamente"
            return redirect(to="analisis")

    return render(request, 'crud_analisis/modificar.html', data)

def listar_analisis(request):
    queruset = request.GET.get("buscar")
    analisis = Analisis.objects.all()

    if queruset:
        analisis = Analisis.objects.filter(
            Q(nombrejuego__icontains = queruset)
        ).distinct()
    
    paginator = Paginator(analisis,10)
    page = request.GET.get('page')
    analisis = paginator.get_page(page)

    data = {
        'analisis': analisis
    }
    return render(request, 'crud_analisis/listar.html', data)

def eliminar_analisis(request, slug):
    analisis = get_object_or_404(Analisis, slug=slug)
    analisis.delete()
    return redirect(to="listar_analisis")

## CRUD FORO##

def agregar_foro(request):
    usuario = get_object_or_404(User, pk=request.user.pk)

    if request.method == 'POST':
        formulario = ForoForm(request.POST)
        if formulario.is_valid():
            formu = formulario.save(commit=False)
            formu.user = usuario
            formu.save()
            return redirect('index')

    else:
        formulario = ForoForm()

    return render(request, 'crud_foro/agregar.html', {'form' : ForoForm})

def modificar_foro(request, slug):
    foro = get_object_or_404(Foro, slug=slug)

    data = {
        'form': ForoForm(instance=foro)
    }

    if request.method == 'POST':
        formulario = ForoForm(data=request.POST, instance=foro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "modificado correctamente"
            return redirect(to="foro")

    return render(request, 'crud_foro/modificar.html', data)

def listar_foro(request):
    queruset = request.GET.get("buscar")
    foro = Foro.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    if queruset:
        foro = Foro.objects.filter(
            Q(tema__icontains = queruset)
        ).distinct()
    
    paginator = Paginator(foro,10)
    page = request.GET.get('page')
    foro = paginator.get_page(page)

    data = {
        'foro': foro
    }

    return render(request, 'crud_foro/listar.html', data)

def eliminar_foro(request, slug):
    foro = get_object_or_404(Foro, slug=slug)
    foro.delete()
    return redirect(to="listar_foro")
#Fin del CRUD#

def agregar_comentario(request):

    data = {
        'form': ComentarioForm()
    }

    if request.method == 'POST':
        formulario = ComentarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            data["mensaje"] = "Guardado Con Exito"
        else:
            data["mensaje"] = "Guardado Con Exito"
            data["form"] = formulario

    return render(request, 'crud_comentario/agregar.html', data)


class UserCreate(CreateView):
    model = User
    fields = ['usuario','apellido','nacimiento','telefono','direccion']

class UserUpdate(UpdateView):
    model = User
    fields = ['usuario','apellido','nacimiento','telefono','direccion']

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('index')

class UserDetailView(generic.DetailView):
    model = User