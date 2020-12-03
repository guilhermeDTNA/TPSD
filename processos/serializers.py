from rest_framework import serializers
from .models import *


class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '__all__'

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'
        
class Entrada_do_CatalogoSerializer(serializers.ModelSerializer):
    entrada = EntradaSerializer()
    catalogo = CatalogoSerializer()
    class Meta:
        model = Entrada_do_catalogo
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class DescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descricao
        fields = '__all__'

class Palavras_ChaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavras_chave
        fields = '__all__'


class CoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobertura
        fields = '__all__'

class EstruturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrutura
        fields = '__all__'

class AgregacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agregacao
        fields ='__all__'



class GeralSerializer(serializers.ModelSerializer):
    Titulo = TituloSerializer()
    Entrada_do_catalogo = Entrada_do_CatalogoSerializer()
    Idioma = IdiomaSerializer()
    Descricao = DescricaoSerializer()
    Palavras_chave = Palavras_ChaveSerializer()
    Cobertura = CoberturaSerializer()
    Estrutura = EstruturaSerializer()
    Agregacao = AgregacaoSerializer()

    class Meta:
        model = Geral
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields ='__all__'

class ContribuicaoSerializer(serializers.ModelSerializer):
    data = DataSerializer()
    class Meta:
        model = Contribuicao
        fields ='__all__'

class Ciclo_De_VidaSerializer(serializers.ModelSerializer):
    contribuicao = ContribuicaoSerializer()
    class Meta:
        model = Ciclo_De_Vida
        fields ='__all__'

class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formato
        fields ='__all__'

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields ='__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    formato = FormatoSerializer()
    tamanho = TamanhoSerializer()
    class Meta:
        model = Tecnico
        fields ='__all__'

class ApiOASerializer(serializers.ModelSerializer):
    Geral = GeralSerializer()
    Ciclo_De_Vida = Ciclo_De_VidaSerializer()
    Tecnico = TecnicoSerializer()
    class Meta:
        model = ApiOA
        fields ='__all__'