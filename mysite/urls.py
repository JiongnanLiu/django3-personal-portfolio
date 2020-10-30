"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from portfolio import views
from stockscreener import views as stock
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # Auth
    path('/signup/', stock.userSignup, name="userSignup"),
    path('logout/', stock.userLogout, name="userLogout"),
    path('/signin/', stock.userLogin, name="userLogin"),
    path('stockscreener/', stock.stockscreener, name="stockscreener"),

    path('blog/', include('blog.urls')),
    path('life/', include('life.urls')),
    path('sudoku/', include('sudoku.urls')),
    path('stockscreener/', include('stockscreener.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
