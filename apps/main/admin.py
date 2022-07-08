from django.contrib import admin

from apps.main.models import Bill, Profile


class BillAdmin(admin.ModelAdmin):
    list_display = ["name", "end_date", "value", "profile"]


admin.site.register(Profile)
admin.site.register(Bill, BillAdmin)
