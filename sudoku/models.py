from django.db import models
from datetime import date
# Create your models here.


class Sudoku(models.Model):
    username = models.CharField(max_length=100)
    profilePic = models.ImageField(upload_to='sudoku/images/')
    time = models.TimeField()
    date = models.DateField(default=date.today)


class Ranking(models.Model):
    name = models.CharField(max_length=100)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    rank = models.IntegerField()

    class Meta:
        db_table = "ranking_panel"
