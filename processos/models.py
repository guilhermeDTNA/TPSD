from django.db import models


class Titulo(models.Model):
    titulo = models.CharField(max_length=255, blank=True, null=True, default='nulo') 
    def __str__(self):
        return self.titulo


class Catalogo(models.Model):
    catalogo = models.CharField(max_length=255, blank=True, null=True, default='nulo')

class Entrada(models.Model):
    entrada = models.CharField(max_length=255, blank=True, null=True, default='nulo')

class Entrada_do_catalogo(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='Catalogo')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='Entrada')


class Idioma(models.Model):
    idioma = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
       return self.idioma


class Descricao(models.Model):
     descricao = models.CharField(max_length=255, blank=True, null=True, default='nulo')
     def __str__(self):
      return self.descricao


class Palavras_chave(models.Model):
    palavras_chaves = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
      return self.palavras_chaves

class Cobertura(models.Model):
    cobertura = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
      return self.cobertura

class Estrutura(models.Model):
    estrutura = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
      return self.estrutura

class Agregacao (models.Model):
    agregacao = models.IntegerField(blank=True, null=True, default='nulo')
    def __str__(self):
      return str(self.agregacao)

class Geral(models.Model):
     Titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE, related_name='Titulo')
     Entrada_do_catalogo = models.ForeignKey(Entrada_do_catalogo, on_delete=models.CASCADE)
     Idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, related_name='Idioma')
     Descricao = models.ForeignKey(Descricao, on_delete=models.CASCADE, related_name='Descricao')
     Palavras_chave = models.ForeignKey(Palavras_chave, on_delete=models.CASCADE, related_name='Palavras_chave')
     Cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE, related_name='Cobertura')
     Estrutura = models.ForeignKey(Estrutura, on_delete=models.CASCADE, related_name='Estrutura')
     Agregacao = models.ForeignKey(Agregacao, on_delete=models.CASCADE, related_name='Agregacao')

class Data(models.Model):
    data = models.DateField(blank=True, null=True)
    def __str__(self):
        return str(self.data)

class Contribuicao(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='Data')
    def __str__(self):
        return str(self.data)

class Ciclo_De_Vida(models.Model):
    contribuicao = models.ForeignKey(Contribuicao, on_delete=models.CASCADE, related_name='Contribuição')
    def __str__(self):
        return str(self.contribuicao)

class Formato(models.Model):
    formato = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
        return self.formato

class Tamanho(models.Model):
    tamanho = models.IntegerField(blank=True, null=True, default=0)
    def __str__(self):
        return str(self.tamanho)

class Tecnico(models.Model):
    formato = models.ForeignKey(Formato, on_delete=models.CASCADE, related_name='Formato')
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, related_name='Tamanho')
    def __str__(self):
        return str(self.tamanho) + str(self.formato)

class ApiOA(models.Model):
    Geral = models.ForeignKey(Geral, on_delete=models.CASCADE, related_name='Geral')
    Ciclo_De_Vida = models.ForeignKey(Ciclo_De_Vida, on_delete=models.CASCADE, related_name='Ciclo_De_Vida')
    Tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='Tecnico')