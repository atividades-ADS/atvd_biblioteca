from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    
    contexto = {'livros': livros}
    
    return render(request, 'biblioteca/listar_livros.html', contexto)

def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    livros = Livro.objects.filter(authors__id=author_id)
    
    contexto = {'author': author, 'livros':livros}
    
    return render(request, 'biblioteca/author_detail.html', contexto)

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            autor = Author(name=form.cleaned_data["name"], nationality=form.cleaned_data["nationality"])
            autor.save()

            return redirect("details_author", autor.id)
    else:
        form = AuthorForm()

    return render(request, "biblioteca/author_create.html", {"form": form})