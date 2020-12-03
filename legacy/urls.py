from django.contrib import admin
from django.urls import path, include
from processos.views import *
from rest_framework import routers


router = routers.DefaultRouter()

'''
router.register('titulo',TituloViewSet)
router.register('entrada_do_catalogo',Entrada_do_CatalogoViewSet)
router.register('entrada',EntradaViewSet)
router.register('catalogo',CatalogoViewSet)
router.register('idioma',IdiomaViewSet)
router.register('descricao',DescricaoViewSet)
router.register('palavras_chave',Palavras_ChaveViewSet)
router.register('cobertura',CoberturaViewSet)
router.register('estrutura',EstruturaViewSet)
router.register('agregacao',AgregacaoViewSet)

router.register('data',DataViewSet)
router.register('contribuicao',ContribuicaoViewSet)
router.register('ciclo_de_vida',Ciclo_De_VidaViewSet)

router.register('formato',FormatoViewSet)
router.register('tamanho',TamanhoViewSet)
router.register('tecnico',TecnicoViewSet)
'''

router.register('ApiOA',ApiOAViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('consulta_objetos', consulta_api),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
