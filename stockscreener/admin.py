from django.contrib import admin
from .models import StockScreener, StockPrice, StockPriceHistory


class StockScreenerAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class StockPriceAdmin(admin.ModelAdmin):
    fields = ['ticker', 'name', 'open', 'close', 'high', 'low', 'volume']


class StockPriceHistoryAdmin(admin.ModelAdmin):
    fields = ['ticker', 'name', 'date', 'close',
              'volume', 'ma20', 'ma60', 'ma120']

    # Register your models here.
admin.site.register(StockScreener, StockScreenerAdmin)
admin.site.register(StockPrice, StockPriceAdmin)
admin.site.register(StockPriceHistory, StockPriceHistoryAdmin)
