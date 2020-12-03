from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def consulta_api(request):
    if request.method == 'GET':
        vetor_parametros = []
        print(request.GET)
        cont = 0
        if request.query_params: #Se contem os parametros na URL
            for i in request.GET.values():
                if i == 'json':
                    continue
                if i != '':
                    vetor_parametros.append(i) #adicionar os valores dos parametros em um vetor
                else:
                    vetor_parametros.append(i)
                print(str(i)+'  '+str(cont))
                cont+=1
            try:

                if vetor_parametros[10] == '': #Se a data não foi informada
                    print(vetor_parametros[10] + '   <<<')
                    members = ApiOA.objects.filter(Geral__Entrada_do_catalogo__catalogo__catalogo__contains =  vetor_parametros[0],
                                                   Geral__Entrada_do_catalogo__entrada__entrada__contains=vetor_parametros[1],
                                                   Geral__Titulo__titulo__contains=vetor_parametros[2],
                                                   Geral__Idioma__idioma__contains= vetor_parametros[3],
                                                   Geral__Descricao__descricao__contains=vetor_parametros[4],
                                                   Geral__Palavras_chave__palavras_chaves__contains=vetor_parametros[5],
                                                   Geral__Cobertura__cobertura__contains=vetor_parametros[6],
                                                   Geral__Estrutura__estrutura__contains=vetor_parametros[7],
                                                   Geral__Agregacao__agregacao__contains=vetor_parametros[8],
                                                   Tecnico__formato__formato__contains = vetor_parametros[9],
                                                   Tecnico__tamanho__tamanho__contains = vetor_parametros[11],)

                    serializer = ApiOASerializer(members, many=True)

                    response = Response(serializer.data, content_type='application/json')
                    #response['Content-Disposition'] = 'attachment; filename=export.json'

                    return Response(serializer.data)                    

                else:
                    members = ApiOA.objects.filter(Geral__Entrada_do_catalogo__catalogo__catalogo__contains =  vetor_parametros[0],
                                                   Geral__Entrada_do_catalogo__entrada__entrada__contains=vetor_parametros[1],
                                                   Geral__Titulo__titulo__contains=vetor_parametros[2],
                                                   Geral__Idioma__idioma__contains= vetor_parametros[3],
                                                   Geral__Descricao__descricao__contains=vetor_parametros[4],
                                                   Geral__Palavras_chave__palavras_chaves__contains=vetor_parametros[5],
                                                   Geral__Cobertura__cobertura__contains=vetor_parametros[6],
                                                   Geral__Estrutura__estrutura__contains=vetor_parametros[7],
                                                   Geral__Agregacao__agregacao__contains=vetor_parametros[8],
                                                   Tecnico__formato__formato__contains = vetor_parametros[9],
                                                   Ciclo_De_Vida__contribuicao__data__data__contains = vetor_parametros[10],
                                                   Tecnico__tamanho__tamanho__contains = vetor_parametros[11],)
                    serializer = ApiOASerializer(members, many=True)
                    response = Response(serializer.data, content_type='application/json')
                    
                    #response['Content-Disposition'] = 'attachment; filename=export.json'
                    return Response(serializer.data)
            except:
                return HttpResponse('<p>Os parametros de pesquisa foram passados errados, utilize a estrutura:</p>'
                                    '<p>http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=</p>')
        else: #Retornar todos os objetos
            members = ApiOA.objects.all()
            serializer = ApiOASerializer(members, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = ApiOASerializer(data=request.id) #Busca o objeto pelo id no parametro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TituloViewSet(viewsets.ModelViewSet):
    queryset = Titulo.objects.all()

    serializer_class = TituloSerializer


class Entrada_do_CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Entrada_do_catalogo.objects.all()

    serializer_class = Entrada_do_CatalogoSerializer

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()

    serializer_class = CatalogoSerializer

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()

    serializer_class = EntradaSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()

    serializer_class = IdiomaSerializer

class DescricaoViewSet(viewsets.ModelViewSet):
    queryset = Descricao.objects.all()

    serializer_class = DescricaoSerializer


class Palavras_ChaveViewSet(viewsets.ModelViewSet):
    queryset = Palavras_chave.objects.all()

    serializer_class = Palavras_ChaveSerializer


class CoberturaViewSet(viewsets.ModelViewSet):
    queryset = Cobertura.objects.all()

    serializer_class = CoberturaSerializer

class EstruturaViewSet(viewsets.ModelViewSet):
    queryset = Estrutura.objects.all()

    serializer_class = EstruturaSerializer

class AgregacaoViewSet(viewsets.ModelViewSet):
    queryset = Agregacao.objects.all()

    serializer_class = AgregacaoSerializer


class GeralViewSet(viewsets.ModelViewSet):
    queryset = Geral.objects.all()

    serializer_class = GeralSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()

    serializer_class = DataSerializer

class ContribuicaoViewSet(viewsets.ModelViewSet):
    queryset = Contribuicao.objects.all()

    serializer_class = ContribuicaoSerializer

class Ciclo_De_VidaViewSet(viewsets.ModelViewSet):
    queryset = Ciclo_De_Vida.objects.all()

    serializer_class = Ciclo_De_VidaSerializer


class TamanhoViewSet(viewsets.ModelViewSet):
    queryset = Tamanho.objects.all()

    serializer_class = TamanhoSerializer

class FormatoViewSet(viewsets.ModelViewSet):
    queryset = Formato.objects.all()

    serializer_class = FormatoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()

    serializer_class = TecnicoSerializer

class ApiOAViewSet(viewsets.ModelViewSet):
    queryset = ApiOA.objects.all()

    serializer_class = ApiOASerializer
