from django.shortcuts import render
from .models import Tarefa
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ListaTarefasView(ListView):
  template_name = 'tarefas/lista_tarefas.html'
  model = Tarefa
  context_object_name = 'tarefas'

class DetalheTarefaView(DetailView):
  template_name = 'tarefas/detalhe_tarefa.html'
  model = Tarefa

class CriarTarefaView(CreateView):
  template_name = 'tarefas/criar_tarefa.html'
  model = Tarefa
  fields = ['titulo', 'descricao','concluida']
  success_url = reverse_lazy('lista_tarefas')

class AtualizarTarefaView(UpdateView):
  template_name = 'tarefas/atualizar_tarefa.html'
  model = Tarefa
  fields = ['titulo', 'descricao','concluida']
  success_url = reverse_lazy('lista_tarefas')

class ExcluirTarefaView(DeleteView):
  template_name = 'tarefas/excluir_tarefa.html'
  model = Tarefa
  success_url = reverse_lazy('lista_tarefas')