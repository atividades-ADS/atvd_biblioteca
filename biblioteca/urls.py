from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.listar_livros, name="livros"),
    path("livro/create/", views.livros_create_modelform, name="criar_livro"),
    path("livro/<int:pk>/edit", views.livros_create_modelform, name="editar_livro"),
    path("autor/<int:author_id>/", views.author_detail, name="autor"),
    path("autor/create/", views.author_create, name="criar_autor"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)