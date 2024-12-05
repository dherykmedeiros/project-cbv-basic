from django.db import models
from datetime import datetime


# Create your models here.

class Tarefa(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(blank=True, null=True)
  concluida = models.BooleanField(default=False)
  data_criacao = models.DateField(default=datetime.now)

  def __str__(self):
    return self.titulo
