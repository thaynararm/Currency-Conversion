from django.db import models

# Armazena as cotações das moedas
class Currency(models.Model):
    from_currency = models.CharField(max_length=3, unique=True, null=False, blank=False)
    to_currency = models.CharField(max_length=3, unique=True, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self) -> str:
        return self.id