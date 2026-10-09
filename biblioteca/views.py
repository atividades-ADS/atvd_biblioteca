from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    
    contexto = {'livros': livros}
    
    return render(request, 'biblioteca/listar_livros.html', contexto)

def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    livros = Livro.objects.filter(author__id=author_id)
    
    contexto = {'author': author, 'livros':livros}
    
    return render(request, 'biblioteca/author_detail.html', contexto)