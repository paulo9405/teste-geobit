from rest_framework.serializers import ModelSerializer
from core.models import Pessoa


class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
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
        ]
