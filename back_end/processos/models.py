from django.db import models


class Geral(models.Model):
    # É definido um default, pois a view não consegue coparar quando o campo no banco está vazio
    catalogo = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    entrada = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    titulo = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    idioma = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    descricao = models.CharField(max_length=500, blank=True, null=True, default='nulo')
    palavras_chaves = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    cobertura = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    estrutura = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    nivel_agregacao = models.IntegerField(blank=True, null=True, default=0)
    formato = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    data = models.DateField(blank=True, null=True)
    tamanho = models.IntegerField(blank=True, null=True, default=0)


    def __str__(self):
        return self.titulo