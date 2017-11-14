from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TarefaManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().filter(models.Q(nome__icontains=query) | models.Q(descricao__icontains=query) | models.Q(categoria__nome__icontains=query), user=user)

class Categoria(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(u'Descrição')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )
    CONCLUIDO = 'C'
    CANCELADA = 'CD'
    STATUS_CHOICES = (
        (CONCLUIDO, 'Concluído'),
        (CANCELADA, 'Cancelada'),
    )
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(u'Descrição', blank=True)
    data_final = models.DateField(u'Data final')
    prioridade = models.CharField(u'Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')
    user = models.ForeignKey(User)
    status = models.CharField(u'Status', max_length=5, choices=STATUS_CHOICES, blank=True, default='')

    objects = TarefaManager()

    def __str__(self):
        return self.nome
