from django.shortcuts import render
from .models import *

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    
    contexto = {
        'livros': livros
    }
    
    return render(request, 'biblioteca/listar_livros.html', contexto)