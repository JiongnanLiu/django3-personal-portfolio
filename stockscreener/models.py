from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class StockScreener(models.Model):
    profilePic = models.ImageField(upload_to='stockscreener/images/')
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(
        max_length=256, unique=True, db_column='email', default=None)

    def __str__(self):
        return self.title


class StockPrice(models.Model):
    ticker = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField(default=0)

    class Meta:
        db_table = 'stock_price_last_day'
        unique_together = [['ticker', 'name']]


class StockPriceHistory(models.Model):
    ticker = models.CharField(default='None', max_length=4)
    name = models.CharField(default='None', max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    close = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    ma20 = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    ma60 = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    ma120 = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    volume = models.IntegerField(default=0)

    class Meta:
        db_table = 'stock_price_history'
