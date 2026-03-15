from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):

    if request.method == "POST":

        Livro.objects.create(
            titulo=request.POST.get("titulo"),
            autor=request.POST.get("autor"),
            editora=request.POST.get("editora"),
            ano_publicacao=request.POST.get("ano_publicacao"),
            numero_paginas=request.POST.get("numero_paginas"),
            categoria=request.POST.get("categoria"),
            isbn=request.POST.get("isbn"),
            idioma=request.POST.get("idioma"),
            edicao=request.POST.get("edicao"),
            descricao=request.POST.get("descricao")
        )

        return redirect("confirmacao")

    return render(request, "cadastro.html")


def confirmacao(request):
    return render(request, "confirmacao.html")

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def consulta(request):
    busca = request.GET.get('buscar')
    resultado = None

    if busca:
        resultado = Livro.objects.filter(titulo__icontains=busca)

    return render(request, 'consulta.html', {'resultado': resultado})

def resultado(request):
    titulo = request.GET.get('titulo')
    livros = None

    if titulo:
        livros = Livro.objects.filter(titulo__icontains=titulo)

    return render(request, 'resultado.html', {'livros': livros})

def detalhes(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    return render(request, 'detalhes.html', {'livro': livro})

def lista(request):
    livros = Livro.objects.all()
    return render(request, 'lista.html', {'livros': livros})

def deletar(request, id):
    livro = get_object_or_404(Livro, id=id)
    
    if request.method == 'POST':
        livro.delete()
        return redirect('lista') 
    
    return render(request, 'deletar.html', {'livro': livro})


