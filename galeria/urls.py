# galeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.photo_detail, name='photo_detail'),
    path('pesquisar/', views.photo_search, name='photo_search'),
]