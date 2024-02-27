from django.contrib import admin
from django.urls import path, include
from conversion.views import CurrencyViewSet
from rest_framework import routers


# Cria uma instância do DefaltRouter - Responsável por manipular as operações CRUD
router = routers.DefaultRouter()
router.register('currency', CurrencyViewSet, basename='currency')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
