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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __init__(self, table):
        self.stocktable = table
