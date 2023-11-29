from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True, default='')
    cpf = models.CharField(max_length=11, unique=True, default='')
    rg = models.CharField(max_length=9, default='')
    telefone = models.CharField(max_length=14, default='')
    celular = models.CharField(max_length=11, default="")
    ativo = models.BooleanField(max_length=1, default=True)

    def __str__(self):
        return self.name
