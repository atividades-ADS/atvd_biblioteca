from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros),
    path('/autor/<int:author_id>/', views.author_detail, name='autor'),
]