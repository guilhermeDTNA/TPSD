from rest_framework import serializers
from .models import Cliente, Geral


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'idade']

class GeralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geral
        fields = ['catalogo', 'entrada',
                  'titulo', 'idioma', 'descricao',
                  'palavras_chaves', 'cobertura',
                  'estrutura', 'nivel_agregacao']