from django.db import models
from datetime import date

# Create your models here.
class Life(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='life/images/')
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)