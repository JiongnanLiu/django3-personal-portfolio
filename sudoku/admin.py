from django.contrib import admin
from .models import Sudoku, Ranking
# Register your models here.


class SudokuAdmin(admin.ModelAdmin):
    field = ['username', 'profilePic', 'time', 'date']


class RankingAdmin(admin.ModelAdmin):
    field = ['name', 'minutes', 'seconds', 'rank']


admin.site.register(Sudoku, SudokuAdmin)
admin.site.register(Ranking, RankingAdmin)
