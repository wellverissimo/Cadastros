from django.urls import path
from CadastroClientes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.listar_clientes, name='clientes')
]