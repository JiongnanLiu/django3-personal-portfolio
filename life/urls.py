from django.urls import include, path
from life import views

app_name='life'

urlpatterns = [
    path('', views.all_photos, name='all_photos'),
    path('<int:photo_id>/', views.detail, name='detail'),
]