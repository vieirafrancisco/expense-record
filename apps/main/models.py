from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        related_name="profile",
    )
    revenue = models.DecimalField(
        max_digits=19, decimal_places=2, default=0, verbose_name="Receita"
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return self.user.username

    def get_purchase_power_amount(self, date):
        if not self.revenue:
            return 0
        bills = self.bills.filter(Q(end_date=None) | Q(end_date__gt=date))
        amount = float(sum(bill.value for bill in bills))
        return round((float(self.revenue) - amount) * 0.90, 2)


class Bill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        related_name="bills",
    )
    name = models.CharField(max_length=254)
    end_date = models.DateField(
        verbose_name="Data de encerramento", null=True, blank=True
    )
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor"
    )

    class Meta:
        verbose_name = "Dívida"
        verbose_name_plural = "Dívidas"

    def __str__(self):
        return self.name


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, *args, **kwargs):
    if kwargs.get("created"):
        Profile.objects.create(user=instance)
