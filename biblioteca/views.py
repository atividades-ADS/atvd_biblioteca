from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy, reverse


class listar_livros(ListView):
    model = Livro
    template_name = "biblioteca/listar_livros.html"
    context_object_name = "livros"
    
    def get_queryset(self):
        return Livro.objects.order_by("titulo")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_livros"] = Livro.objects.count()
        context["total_livros_disponivels"] = Livro.objects.filter(disponivel=True).count()
        return context

class author_details(DetailView):
    model = Author
    template_name = "biblioteca/author_detail.html"

class author_create(CreateView):
    model = Author
    fields = ["name", "nationality"]
    template_name = "biblioteca/author_create.html"
    
    def get_success_url(self):
        return reverse("details_author", kwargs={"pk": self.object.pk})

class livro_create_or_edit(CreateView, UpdateView):
    model = Livro
    form_class = LivroModelForm
    template_name = "biblioteca/forms_livros.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return super().get_object(queryset) if pk else None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        has_pk = bool(self.kwargs.get("pk"))
        context["page_intent"] = "Editar livro" if has_pk else "Criar livro"
        context["page_title"] = "Editar" if has_pk else "Criar"
        return context

    def get_success_url(self):
        author_id = self.kwargs.get("author_id")
        if author_id:
            return reverse("details_author", kwargs={"pk": author_id})
        return reverse("listar_livros")

class livro_delete(DeleteView):
    model = Livro
    success_url = reverse_lazy("listar_livros")

class sobre(TemplateView):
    template_name = "biblioteca/about.html"