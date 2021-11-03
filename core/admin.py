from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'sobrenome',
        'sexo',
        'altura',
        'peso',
        'nascimento',
        'bairro',
        'cidade',
        'estado',
        'numero'
    )


admin.site.register(Pessoa, PessoaAdmin)
