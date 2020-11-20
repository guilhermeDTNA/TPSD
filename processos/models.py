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

