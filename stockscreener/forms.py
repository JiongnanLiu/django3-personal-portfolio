from django.forms import ModelForm
from .models import StockScreener


class StockScreenerForm(ModelForm):
    class Meta:
        model = StockScreener
        fields = ['title', 'memo', 'important']
