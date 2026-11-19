from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros.as_view(), name="listar_livros"),
    path('detalhes/<int:pk>', views.author_details.as_view(), name="details_author"),
    path('criarAutor', views.author_create.as_view(), name="create_author"),
    path("new/", views.livro_create_or_edit.as_view(), name="livro_create"),
    path("<int:pk>/edit/", views.livro_create_or_edit.as_view(), name="livro_edit"),
    path("<int:pk>/<int:author_id>/edit/", views.livro_create_or_edit.as_view(), name="livro_edit_author"),
    path("<int:pk>/delete/", views.livro_delete.as_view(), name="livro_delete"),
    path("sobre/", views.sobre.as_view(), name="sobre"),
]