from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static
from .views import agregar_noticia, modificar_noticia, eliminar_noticia, listar_noticia, agregar_analisis, modificar_analisis, eliminar_analisis, listar_analisis, agregar_foro, modificar_foro, eliminar_foro, listar_foro, agregar_comentario


urlpatterns = [
    path('',views.index,name='index'),
    path('noticias',views.noticias,name='noticias'),
    path('analisis',views.analisis,name='analisis'),
    path('foro',views.foro,name='foro'),
    path('detallePost/<slug:slug>/', views.detallePost, name='detalle_post'),
    path('analisisPost/<slug:slug>/', views.analisisPost, name='analisis_post'),
    path('foroPost/<slug:slug>/', views.foroPost, name='foro_post'),#?#
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user_detail'),
    #CRUD NOTICIA#    
    path('agregar-noticia/', agregar_noticia, name="agregar_noticia"),
    path('modificar-noticia/<slug:slug>/', modificar_noticia, name="modificar_noticia"),
    path('eliminar-noticia/<slug:slug>/', eliminar_noticia, name="eliminar_noticia"),
    path('listar-noticia/', listar_noticia, name="listar_noticia"),
    #CRUD ANALISIS#    
    path('agregar-analisis/', agregar_analisis, name="agregar_analisis"),
    path('modificar-analisis/<slug:slug>/', modificar_analisis, name="modificar_analisis"),
    path('eliminar-analisis/<slug:slug>/', eliminar_analisis, name="eliminar_analisis"),
    path('listar-analisis/', listar_analisis, name="listar_analisis"),
    #CRUD FORO#    
    path('agregar-foro/', agregar_foro, name="agregar_foro"),
    path('modificar-foro/<slug:slug>/', modificar_foro, name="modificar_foro"),
    path('eliminar-foro/<slug:slug>/', eliminar_foro, name="eliminar_foro"),
    path('listar-foro/', listar_foro, name="listar_foro"),
    #CRUD Comentario#
    path('agregar-comentario/', agregar_comentario, name="agregar_comentario"),
]

urlpatterns += [
    path('crear_usuario',views.UserCreate.as_view(),name='user_form'),
    path('user/<int:pk>/update/',views.UserUpdate.as_view(),name='user_update'),
    path('user/<int:pk>/delete/',views.UserDelete.as_view(),name='user_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
