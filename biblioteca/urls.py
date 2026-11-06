from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name="listar_livros"),
    path('detalhes/<int:author_id>', views.author_details, name="details_author"),
    path('criarAutor', views.author_create, name="create_author"),
]