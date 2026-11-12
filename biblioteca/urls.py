from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name="listar_livros"),
    path('detalhes/<int:author_id>', views.author_details, name="details_author"),
    path('criarAutor', views.author_create, name="create_author"),
    path("new/", views.livro_create_or_edit, name="livro_create"),
    path("<int:pk>/edit/", views.livro_create_or_edit, name="livro_edit"),
    path("<int:pk>/<int:author_id>/edit/", views.livro_create_or_edit, name="livro_edit_author"),
]