from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todo.tarefas.models import Tarefa

# Create your views here.

@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user, status='')
    return render(request, 'core/index.html', {'tarefas': tarefas})
