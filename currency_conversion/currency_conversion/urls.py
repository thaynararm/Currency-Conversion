from django.contrib import admin
from django.urls import path, include
from conversion.views import CurrencyConverterView
from rest_framework import routers


# Cria uma instância do DefaltRouter - Responsável por manipular as operações CRUD
#router = routers.DefaultRouter()
#router.register('', CurrencyViewSet, basename='currency')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    path('', CurrencyConverterView.as_view(), name='convert_currency'),
]
