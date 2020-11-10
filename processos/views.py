from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import GeralSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class GeralViewSet(viewsets.ModelViewSet):
    queryset = Geral.objects.all()
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