from django.contrib import admin
from .models import *

admin.site.register(Titulo)
admin.site.register(Entrada_do_catalogo)
admin.site.register(Catalogo)
admin.site.register(Entrada)
admin.site.register(Idioma)
admin.site.register(Descricao)
admin.site.register(Palavras_chave)
admin.site.register(Cobertura)
admin.site.register(Estrutura)
admin.site.register(Agregacao)
admin.site.register(Geral)

admin.site.register(Data)
admin.site.register(Contribuicao)
admin.site.register(Ciclo_De_Vida)

admin.site.register(Formato)
admin.site.register(Tamanho)
admin.site.register(Tecnico)

admin.site.register(ApiOA)