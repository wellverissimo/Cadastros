from django.urls import path
from CadastroClientes import views

urlpatterns = [
    path('', views.index, name='index'),
]