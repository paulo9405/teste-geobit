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