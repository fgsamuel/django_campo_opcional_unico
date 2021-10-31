from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, blank=True, null=True, default=None, unique=True)
    email = models.EmailField(blank=True, null=True, default=None, unique=True)

    def __str__(self):
        return self.nome
