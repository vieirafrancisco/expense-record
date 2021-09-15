from datetime import date

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
        return f"Cartão de Crédito ({self.name})"


class Bill(models.Model):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, verbose_name="Cartão de Crédito")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(verbose_name="Data")
    value = models.DecimalField(verbose_name="Valor", decimal_places=2, max_digits=19)
    is_service = models.BooleanField(default=False, verbose_name="É um serviço?")
    end_service_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de finalização do Serviço")
    is_installment = models.BooleanField(default=False, verbose_name="É parcelado?")
    installment_count = models.SmallIntegerField(default=0, verbose_name="Número de parcelas")
    has_promotion = models.BooleanField(default=False, verbose_name="Tem promoção?")
    promotion_count = models.SmallIntegerField(default=0, verbose_name="Número de mêses com a promoção")

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
        constraints = [
            models.CheckConstraint(
                check=~(models.Q(is_service=True) & models.Q(is_installment=True)),
                name="Service and Installmente can't both be True."
            ),
        ]

    def __str__(self):
        return f"Conta ({self.name}) do {self.credit_card}"
    
    @property
    def promotion_due_date(self):
        if self.has_promotion:
            day = self.date.day
            month = (self.date.month + self.promotion_count) % 12
            year = self.date.year + (self.date.month + self.promotion_count) // 12
            return date(day=day, month=month, year=year)
