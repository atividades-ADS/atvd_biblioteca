from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros),
    path('detalhes/<int:author_id>', views.author_details, name="details_author")
]