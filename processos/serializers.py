from rest_framework import serializers
from .models import *

class GeralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geral
        fields = ['catalogo', 'entrada',
                  'titulo', 'idioma', 'descricao',
                  'palavras_chaves', 'cobertura',
                  'estrutura', 'nivel_agregacao', 'formato','data', 'tamanho']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf','contato']

class ServicoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Servico
        fields = ['cliente', 'nomeServico','descricao','valor','Desconto','parcelamento']

class ProjetoSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer()
    class Meta:
        model = Projeto
        fields = ['servico', 'dataEntrega','status','responsaveis']