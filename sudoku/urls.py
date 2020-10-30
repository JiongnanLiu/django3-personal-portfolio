from django.urls import include, path
from sudoku import views
#from django.conf.urls import url
#from .import views

app_name = 'sudoku'

urlpatterns = [
    path('', views.sudoku, name='sudoku'),
]
