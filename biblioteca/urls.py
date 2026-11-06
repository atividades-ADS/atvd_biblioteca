from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_livros, name="livros"),
    path("/livro/create/", views.livros_create, name="criar_livro"),
    path("/autor/<int:author_id>/", views.author_detail, name="autor"),
    path("/autor/create/", views.author_create, name="criar_autor"),
]
