from django.shortcuts import render
from CadastroClientes.models import Cliente

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
    # o dicionário (variável) context é que vai mandar pro template
    context = {
        "clientes": lista_clientes,
    }


    return render(request, 'lista_clientes.html', context)