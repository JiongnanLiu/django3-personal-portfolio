from django.urls import re_path, path
from stockscreener import views

app_name = 'stockscreener'
urlpatterns = [
    path('', views.stockscreener, name='stockscreener'),
]
