from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'idade']