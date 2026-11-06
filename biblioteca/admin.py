from django.contrib import admin
from .models import Livro, Author, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "authors__name", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "authors__name", ]
    list_filter = ["disponivel", "categories"]
    filter_horizontal = ["categories"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality"]
