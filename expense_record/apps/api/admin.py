from django.contrib import admin

from .models import CreditCard, Bill

admin.site.register(CreditCard)
admin.site.register(Bill)
