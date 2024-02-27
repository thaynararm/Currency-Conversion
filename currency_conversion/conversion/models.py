from django.db import models

# Armazena as cotações das moedas
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, null=False)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.code