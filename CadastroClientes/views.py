from django.shortcuts import render
from CadastroClientes.models import * #esse asterisco é um "coringa" onde ele busca todos os elementos sem precisar especificar nenhum

# Create your views here.
def index(request):
    meu_nome = 'Wellington Verissimo'
    lista_frutas = ['Laranja', 'Maçã','Banana','Uva','Pera']
    context = {
        'nome': meu_nome,
        'frutas' : lista_frutas
    }
    return render(request, 'index.html', context)

def listar_clientes(request):
    # busca todos os clientes cadastrados na tabela(admin)
    lista_clientes = Cliente.objects.all()
    lista_profissoes = Profissao.objects.all()
    # o dicionário (variável) context é que vai mandar pro template
    context = {
        "clientes": lista_clientes,
        'profissoes': lista_profissoes,
    }
    return render(request, 'lista_clientes.html', context)

def listar_profissoes(request):

    lista_profissoes = Profissao.objects.all()

    context = {
        'profissoes': lista_profissoes,
    }
    return render(request, 'lista_profissoes.html', context)
    
