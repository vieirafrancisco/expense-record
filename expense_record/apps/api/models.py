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
    is_installment = models.BooleanField(default=False, verbose_name="É parcelado?")

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
        constraints = [
            models.CheckConstraint(
                check=~(models.Q(is_service=True) & models.Q(is_installment=True)),
                name="Service and Installmente can't both be True."
            ),
        ]
        unique_together = (("credit_card", "name", "date"),)

    def __str__(self):
        return f"Conta ({self.name}) do {self.credit_card}"

    def create(self, data):
        pass
    

class Service(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, verbose_name="Conta")
    is_active = models.BooleanField(default=True, verbose_name="Está ativo?")
    end_date = models.DateField(null=True, blank=True, verbose_name="Data de finalização do serviço")
    has_promotion = models.BooleanField(default=False, verbose_name="Tem promoção?")
    promotion_count = models.SmallIntegerField(default=0, verbose_name="Número de meses com a promoção")
    # TODO: valor após a promoção

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return f"Serviço da {self.bill}"
    
    @property
    def promotion_due_date(self):
        # TODO: fix this method
        bill_date = self.bill.date
        if self.has_promotion:
            day = bill_date.day
            month = (bill_date.month + self.promotion_count) % 12  # WARNING: wrong
            year = bill_date.year + (bill_date.month + self.promotion_count) // 12
            return date(day=day, month=month, year=year)


class Installment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, verbose_name="Conta")
    count = models.SmallIntegerField(verbose_name="Número de parcelas")

    class Meta:
        verbose_name = "Parcelamento"
        verbose_name_plural = "Parcelamentos"

    def __str__(self):
        return f"Parcelamento da {self.bill}"
    
    @property
    def total_value(self):
        return self.bill.value * self.count
    
    @property
    def end_date(self):
        pass
