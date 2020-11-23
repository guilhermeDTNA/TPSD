from django.db import models

FUNCAO_CHOICE_SERVICO = (
    ('SPA','Single Page Application'),
    ('PWA','Progressive Web Application'),
    ('WS', 'WebSite'),
    ('SW', 'Sistema Web'),
    ('IV', 'Identidade Visual'),
)

STATUS = (
    (0, 'Iniciado'),
    (1, 'Em andamento'),
    (2, 'Pendente'),
    (3, 'Resolvido'),
)

FUNCAO_CHOICE_PARCELAMENTO = (
    (1,'01-A VISTA'),
    (2,'02'),
    (3, '03'),
    (4, '04'),
    (5, '05'),
    (6, '06'),
    (7, '07'),
    (8, '08'),
    (9, '09'),
    (10, '10'),
    (11, '11'),
    (12, '12'),

)

class Cliente(models.Model):

    nome = models.CharField('Nome', max_length=40, null=True, blank=True)
    cpf = models.CharField('CPF/CNPJ', max_length=15, null=True, blank=True)
    contato = models.CharField('Contato', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural = ("Clientes")

    def __str__(self):
        return self.nome

class Servico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Cliente')
    nomeServico = models.CharField('Serviço', max_length=4, choices=FUNCAO_CHOICE_SERVICO)
    descricao = models.TextField('Descrição', null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    Desconto = models.DecimalField('Desconto',max_digits=6, decimal_places=2)
    parcelamento = models.IntegerField('Parcelado', choices=FUNCAO_CHOICE_PARCELAMENTO)

    def valorFinal(self):
        return str(self.valor - self.Desconto)

    def __str__(self):
        return self.nomeServico + ' - ' + str(self.cliente) + ' - R$' + str(self.valor - self.Desconto) + ' - ' + str(self.parcelamento) + 'x'


class Projeto(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='Servicos')
    dataEntrega = models.DateField('Entrega', blank=True, null=True)
    status = models.IntegerField('Status', choices=STATUS)
    responsaveis = models.ManyToManyField('Cliente', null=True, blank=True, related_name="responsaveis")


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
    agregacao = models.CharField(max_length=255, blank=True, null=True, default='nulo')
    def __str__(self):
      return self.agregacao

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