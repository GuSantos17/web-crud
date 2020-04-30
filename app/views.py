from django.shortcuts import render, redirect
from .models import Produto
from django.http import Http404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def produtos_list(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Produto.objects.all()
    except:
         data['error'].append("Erro ao carregar produto! ")
    return render(request, 'produtos.html', data)
@csrf_exempt
def new_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        nome = request.POST.get('name')
        quantidade = request.POST.get('qtd')
        valor = request.POST.get('valor')
        try:
            if (id == -1):
                product = Produto(name=nome, quantity=quantidade, value=valor)
                product.save()
            else:
                product = Produto.objects.get(id=id)
                product.name = nome
                product.quantity = quantidade
                product.value = valor
                product.save()
        except:
            data['error'].append("Erro ao cadastrar produto! ")
            return render(request, 'produtos.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produtos.html', data)
        return render(request, 'produtos.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'produtos.html', data)

def delete_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            prod = Produto.objects.get(id=id)
            prod.delete()
        except:
            data['error'].append("Erro ao deletar produto! ")
            return render(request, 'produtos.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produtos.html', data)
        return render(request, 'produtos.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'produtos.html', data)
  
def update_produto(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['product'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['product'].append(Produto.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produtos.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar produtos! ")
            return render(request, 'produtos.html', data)
        return render(request, 'produtos.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente mais tarde! ")
        return render(request, 'produtos.html', data)