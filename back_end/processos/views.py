from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Geral
from .serializers import GeralSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class GeralViewSet(viewsets.ModelViewSet):
    teste = "titulo__contains"
    queryset = Geral.objects.filter(titulo__contains='titul', cobertura__contains='')

    serializer_class = GeralSerializer

@api_view(['GET', 'POST'])
def geral_api(request):
    if request.method == 'GET':
        members = Geral.objects.all()
        serializer = GeralSerializer(members, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GeralSerializer(data=request.id) #Busca o objeto pelo id no parametro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def consulta_api(request):
    if request.method == 'GET':
        vetor_parametros = []
        print(request.GET)

        if request.query_params: #Se contem os parametros na URL
            for i in request.GET.values():
                if i == 'json':
                    continue
                vetor_parametros.append(i) #adicionar os valores dos parametros em um vetor

            try:
                if vetor_parametros[9] == '': #Se a data não foi informada
                    members = Geral.objects.filter(catalogo__contains=vetor_parametros[0],
                                                   entrada__contains=vetor_parametros[1],
                                                   titulo__contains=vetor_parametros[2],
                                                   idioma__contains= vetor_parametros[3],
                                                   descricao__contains=vetor_parametros[4],
                                                   palavras_chaves__contains=vetor_parametros[5],
                                                   cobertura__contains=vetor_parametros[6],
                                                   estrutura__contains=vetor_parametros[7],
                                                   nivel_agregacao__contains=vetor_parametros[8],)
                    serializer = GeralSerializer(members, many=True)
                    return Response(serializer.data)
                else:
                    members = Geral.objects.filter(catalogo__contains=vetor_parametros[0],
                                                   entrada__contains=vetor_parametros[1],
                                                   titulo__contains=vetor_parametros[2],
                                                   idioma__contains= vetor_parametros[3],
                                                   descricao__contains=vetor_parametros[4],
                                                   palavras_chaves__contains=vetor_parametros[5],
                                                   cobertura__contains=vetor_parametros[6],
                                                   estrutura__contains=vetor_parametros[7],
                                                   nivel_agregacao__contains=vetor_parametros[8],
                                                   data=vetor_parametros[9])
                    serializer = GeralSerializer(members, many=True)
                    return Response(serializer.data)
            except:
                return HttpResponse('<p>Os parametros de pesquisa foram passados errados, utilize a estrutura:</p>'
                                    '<p>localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&data=</p>')
        else: #Retornar todos os objetos
            members = Geral.objects.all()
            serializer = GeralSerializer(members, many=True)
            return Response(serializer.data)

    if request.method == 'POST':
        serializer = GeralSerializer(data=request.id) #Busca o objeto pelo id no parametro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def testeview(request):
    if request.method == 'GET':
        pass
        #print(request.GET.get('fname'))
        #print(request.GET)
    for k in request.GET.items():
        print(k)



    return render(request,'testetemplate.html')