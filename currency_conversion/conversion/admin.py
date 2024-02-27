from django.contrib import admin
from conversion.models import Currency

# Visualização do modelo no Admin
class ListingCurrency(admin.ModelAdmin):
    list_display = ('code', 'rate',)
    list_display_links = ('code',)
    search_fields = ('code',)
    list_per_page = 25

admin.site.register(Currency, ListingCurrency)
