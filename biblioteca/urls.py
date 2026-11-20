from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # CRUD de livros
    path("", views.Listar_livros.as_view(), name="livros"),
    path("livro/<int:pk>/", views.Livro_detail.as_view(), name="livro"),
    path("livro/create/", views.Livros_create.as_view(), name="criar_livro"),
    path("livro/<int:pk>/edit", views.Livros_edit.as_view(), name="editar_livro"),
    path("livro/<int:pk>/delete", views.Livros_delete.as_view(), name="excluir_livro"),
    # CRUD de autores
    path("autor/<int:pk>/", views.Author_detail.as_view(), name="autor"),
    path("autor/create/", views.Author_create.as_view(), name="criar_autor"),
    path("autor/<int:pk>/edit", views.Author_edit.as_view(), name="editar_autor"),
    # Sobre 
    path("sobre/", views.sobre.as_view(), name="sobre"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)