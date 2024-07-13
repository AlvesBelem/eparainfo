from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Nome: {self.nome} | Email: {self.email}"
    