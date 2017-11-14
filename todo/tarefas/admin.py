from django.contrib import admin

from .models import Categoria, Tarefa

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_final', 'prioridade', 'categoria')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
