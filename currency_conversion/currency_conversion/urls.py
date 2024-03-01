from django.contrib import admin
from django.urls import path, include
from conversion.views import CurrencyConverterViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CurrencyConverterViewSet.as_view({'post': 'create'}), name='convert_currency'),
]



