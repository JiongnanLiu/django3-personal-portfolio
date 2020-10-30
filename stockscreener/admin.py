from django.contrib import admin
from .models import StockScreener


class StockScreenerAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(StockScreener, StockScreenerAdmin)
