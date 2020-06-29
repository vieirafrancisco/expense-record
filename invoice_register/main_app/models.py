from django.db import models
from django.contrib.auth.models import User

from settings import *

# Create your models here.

class CreditCard(models.Model):
    name = models.CharField(unique=True, max_length=50)
    invoice_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_month_amount(self):
        pass

class Service(models.Model):
    name = models.CharField(unique=True, max_length=50)
    payment_date = models.DateTimeField()
    value = models.FloatField()
    period = models.IntegerField(default=MONTH)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)