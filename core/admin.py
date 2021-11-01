from django.contrib import admin
from .models import Estado, Cidade, Bairro, Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'sobrenome', 'sexo', 'altura', 'peso', 'nascimento', 'bairro'
    )


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
