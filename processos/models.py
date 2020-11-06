from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Geral(models.Model):
    catalogo = models.CharField(max_length=255, blank=True, null=True)
    entrada = models.CharField(max_length=255, blank=True, null=True)
    titulo = models.CharField(max_length=255)
    idioma = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    palavras_chaves = models.CharField(max_length=255, blank=True, null=True)
    cobertura = models.CharField(max_length=255, blank=True, null=True)
    estrutura = models.CharField(max_length=255, blank=True, null=True)
    nivel_agregacao = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo