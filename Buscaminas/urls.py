from django.urls import path
from Buscaminas import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('crea_tablero/', views.crea_tablero, name='crea_tablero'),

]