from django.contrib import admin
from conversion.models import Currency

# Visualização do modelo no Admin
class ListingCurrency(admin.ModelAdmin):
    list_display = ('from_currency', 'to_currency', 'amount')
    list_display_links = ('from_currency',)
    search_fields = ('from_currency',)
    list_per_page = 25

admin.site.register(Currency, ListingCurrency)
