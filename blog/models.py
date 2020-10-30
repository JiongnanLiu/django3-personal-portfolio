from django.db import models
from datetime import date
# Create your models here.
class myBlog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
