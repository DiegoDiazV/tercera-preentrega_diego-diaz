from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('clientes', views.clientes, name="Clientes"),
    path('productos', views.productos, name="Productos"),
    path('categorias', views.categorias, name="Categorias")
]
