from django.urls import path
from .views import *

urlpatterns = [
    path('', ListaTarefasView.as_view(), name='lista_tarefas'),
    path('tarefa/<int:pk>/', DetalheTarefaView.as_view(), name='detalhe_tarefa'),
    path('tarefa/novo', CriarTarefaView.as_view(), name='criar_tarefa'),
    path('tarefa/<int:pk>/editar', AtualizarTarefaView.as_view(), name='atualizar_tarefa'),
    path('tarefa/<int:pk>/excluir', ExcluirTarefaView.as_view(), name='excluir_tarefa' )
]
