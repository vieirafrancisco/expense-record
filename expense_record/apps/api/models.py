from django.db import models
from django.contrib.auth.models import User


class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    invoice_close_day = models.IntegerField(verbose_name="Dia de fechamento da Fatura")

    class Meta:
        verbose_name = "Cartão de Crédito"
        verbose_name_plural = "Cartões de Crédito"
        unique_together = (("user", "name"),)

    def __str__(self):
        return f"CreditCard ({self.name})"
