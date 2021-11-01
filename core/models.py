from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100, null=True)

    # class Meta:
    #     unique_together = ('nome',)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


class Bairro(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)
    numero = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True)
    sexo = models.CharField(max_length=100) # ver dps a possibilidade d e colocar um choice
    altura = models.IntegerField()
    peso = models.DecimalField(max_digits=7, decimal_places=1)
    nascimento = models.CharField(max_length=100) # converter para data
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
