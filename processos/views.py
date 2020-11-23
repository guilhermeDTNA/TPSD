from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# class GeralViewSet(viewsets.ModelViewSet):
#     teste = "titulo__contains"
#     queryset = Geral.objects.filter(titulo__contains='titul', cobertura__contains='')
#
#     serializer_class = GeralSerializer

# @api_view(['GET', 'POST'])
# def geral_api(request):
#     if request.method == 'GET':
#         members = Geral.objects.all()
#         serializer = GeralSerializer(members, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = GeralSerializer(data=request.id) #Busca o objeto pelo id no parametro
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def consulta_api(request):
#     if request.method == 'GET':
#         vetor_parametros = []
#         print(request.GET)
#         cont = 0
#         if request.query_params: #Se contem os parametros na URL
#             for i in request.GET.values():
#                 if i == 'json':
#                     continue
#                 if i != '':
#                     vetor_parametros.append(i) #adicionar os valores dos parametros em um vetor
#                 else:
#                     vetor_parametros.append(i)
#                 print(str(i)+'  '+str(cont))
#                 cont+=1
#             try:
#
#                 if vetor_parametros[10] == '': #Se a data não foi informada
#                     print(vetor_parametros[10] + '   <<<')
#                     members = Geral.objects.filter(catalogo__contains=vetor_parametros[0],
#                                                    entrada__contains=vetor_parametros[1],
#                                                    titulo__contains=vetor_parametros[2],
#                                                    idioma__contains= vetor_parametros[3],
#                                                    descricao__contains=vetor_parametros[4],
#                                                    palavras_chaves__contains=vetor_parametros[5],
#                                                    cobertura__contains=vetor_parametros[6],
#                                                    estrutura__contains=vetor_parametros[7],
#                                                    nivel_agregacao__contains=vetor_parametros[8],
#                                                    formato__contains = vetor_parametros[9],
#                                                    tamanho__contains = vetor_parametros[11],)
#                     serializer = GeralSerializer(members, many=True)
#                     return Response(serializer.data)
#                 else:
#                     members = Geral.objects.filter(catalogo__contains=vetor_parametros[0],
#                                                    entrada__contains=vetor_parametros[1],
#                                                    titulo__contains=vetor_parametros[2],
#                                                    idioma__contains= vetor_parametros[3],
#                                                    descricao__contains=vetor_parametros[4],
#                                                    palavras_chaves__contains=vetor_parametros[5],
#                                                    cobertura__contains=vetor_parametros[6],
#                                                    estrutura__contains=vetor_parametros[7],
#                                                    nivel_agregacao__contains=vetor_parametros[8],
#                                                    formato__contains=vetor_parametros[9],
#                                                    data=vetor_parametros[10],
#                                                    tamanho__contains=vetor_parametros[11],)
#                     serializer = GeralSerializer(members, many=True)
#                     return Response(serializer.data)
#             except:
#                 return HttpResponse('<p>Os parametros de pesquisa foram passados errados, utilize a estrutura:</p>'
#                                     '<p>http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=</p>')
#         else: #Retornar todos os objetos
#             members = Geral.objects.all()
#             serializer = GeralSerializer(members, many=True)
#             return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = GeralSerializer(data=request.id) #Busca o objeto pelo id no parametro
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def testeview(request):
    if request.method == 'GET':
        pass
        #print(request.GET.get('fname'))
        #print(request.GET)
    for k in request.GET.items():
        print(k)



    return render(request,'testetemplate.html')


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()

    serializer_class = ServicoSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()

    serializer_class = ProjetoSerializer




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