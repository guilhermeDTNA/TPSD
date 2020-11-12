from rest_framework import serializers
from .models import Geral

class GeralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geral
        fields = ['catalogo', 'entrada',
                  'titulo', 'idioma', 'descricao',
                  'palavras_chaves', 'cobertura',
                  'estrutura', 'nivel_agregacao', 'data']