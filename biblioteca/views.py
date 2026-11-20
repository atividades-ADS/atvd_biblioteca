from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from .models import *
from .forms import *

# Create your views here.

"""
def listar_livros(request):
    books = Book.objects.all()
    
    contexto = {
        'books': books
    }
    
    return render(request, 'biblioteca/listar_livros.html', contexto)


def livros_create(request):
    if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                Book.objects.create(
                    title = form.cleaned_data["title"],
                    author = form.cleaned_data["author"],
                    category = form.cleaned_data["category"],
                    year = form.cleaned_data["year"],
                    available = form.cleaned_data["available"],
                )
                return redirect("livros")
    else:
        form = BookForm()
        
    return render(request, "biblioteca/criar_livro.html", {"form": form})
    
    
def livros_create_modelform(request, pk=None, ):
    if pk:
        book = get_object_or_404(Book, pk=pk)
        titulo_pagina = "Editar livro"
        texto_botao = "Editar"
    else: 
        book = Book()
        titulo_pagina = "Criar livro"
        texto_botao = "Criar"
    
    next_url = request.POST.get('next') or request.GET.get('next', '')
        
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            with transaction.atomic():
                book = form.save()
            
            # Valida se a URL é segura e pertence ao seu próprio site
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            
            return redirect("livros")
    else:
        form = BookModelForm(instance=book)
    context = {"form": form, "titulo_pagina": titulo_pagina, "texto_botao": texto_botao, "next": next_url,}
    return render(request, "biblioteca/criar_livro.html", context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(authors=author)
    
    contexto = {
        'author': author,
        'books': books
    }
    
    return render(request, 'biblioteca/autor.html', contexto)

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author =Author.objects.create(
                name = form.cleaned_data["name"],
                nationality = form.cleaned_data["nationality"] 
            )
            return redirect("autor", author_id=author.pk)
    else:
        form = AuthorForm()
    
    return render(request, "biblioteca/criar_autor.html", {"form": form})
"""


class Listar_livros(ListView):
    model = Book
    template_name = 'biblioteca/listar_livros.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.order_by("-title")[:10]
    
class Livro_detail(DetailView):
    model = Book
    template_name = 'biblioteca/livro.html'
    context_object_name = 'book'
    pk_url_kwarg = 'pk'
    

class Livros_create(CreateView):
    model = Book
    form_class = BookModelForm
    template_name = 'biblioteca/criar_livro.html'
    success_url = reverse_lazy('livros')
    
class Livros_edit(UpdateView):
    model = Book
    form_class = BookModelForm
    template_name = 'biblioteca/criar_livro.html'
    success_url = reverse_lazy('livros')


class Livros_delete(DeleteView):
    model = Book
    success_url = reverse_lazy('livros')

class Listar_autores(ListView):
    model = Author
    template_name = 'biblioteca/listar_autores.html'
    context_object_name = 'authors'
    
class Author_detail(DetailView):
    model = Author
    template_name = 'biblioteca/autor.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'
    
class Author_create(CreateView):
    model = Author
    form_class = AuthorModelForm
    template_name = 'biblioteca/criar_autor.html'
    success_url = reverse_lazy('livros')
    
class Author_edit(UpdateView):
    model = Author
    form_class = AuthorModelForm
    template_name = 'biblioteca/criar_autor.html'
    success_url = reverse_lazy('livros')
    
    
    
class sobre(TemplateView):
    template_name = 'biblioteca/sobre.html'
    