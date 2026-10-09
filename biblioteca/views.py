from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def listar_livros(request):
    books = Book.objects.all()
    
    contexto = {
        'books': books
    }
    
    return render(request, 'biblioteca/listar_livros.html', contexto)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(authors=author)
    
    contexto = {
        'author': author,
        'books': books
    }
    
    return render(request, 'biblioteca/autor.html', contexto)