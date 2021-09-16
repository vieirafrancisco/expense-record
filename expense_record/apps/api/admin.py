from django.contrib import admin

from .models import CreditCard, Bill, Service, Installment

admin.site.register(CreditCard)
admin.site.register(Bill)
admin.site.register(Service)
admin.site.register(Installment)
