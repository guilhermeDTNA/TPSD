from django.contrib import admin
from django.urls import path, include
from processos.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
