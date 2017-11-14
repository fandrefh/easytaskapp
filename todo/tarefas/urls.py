from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^lista-categorias/$', views.lista_categorias, name='lista_categorias'),
    url(r'^nova-categoria/$', views.nova_categoria, name='nova_categoria'),
    url(r'^editar-categoria/(?P<id_categoria>[0-9]+)/$', views.editar_categoria, name='editar_categoria'),
    url(r'^delete-categoria/(?P<id_categoria>[0-9]+)/$', views.delete_categoria, name='delete_categoria'),
    url(r'^nova-tarefa/$', views.nova_tarefa, name='nova_tarefa'),
    url(r'^editar-tarefa/(?P<id_tarefa>[0-9]+)/$', views.editar_tarefa, name='editar_tarefa'),
    url(r'^delete-tarefa/(?P<id_tarefa>[0-9]+)/$', views.delete_tarefa, name='delete_tarefa'),
    url(r'^detalhes-tarefa/(?P<id_tarefa>[0-9]+)/$', views.detalhes_tarefa, name='detalhes_tarefa'),
    url(r'^buscar/$', views.search, name='search'),
]
