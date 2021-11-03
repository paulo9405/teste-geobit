from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True, null=True)
    TIPO = (('M', 'M'), ('F', 'F'),)
    sexo = models.CharField(max_length=1, choices=TIPO, null=True)
    altura = models.IntegerField()
    peso = models.DecimalField(max_digits=7, decimal_places=1)
    nascimento = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return self.nome
