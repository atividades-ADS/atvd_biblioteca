from django.contrib import admin
from .models import Livro, Author, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "author", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "author", ]
    list_filter = ["disponivel", "categories"]
    filter_horizontal = ["categories"]

class LivrosInline(admin.TabularInline):
    model = Livro
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality"]
    inlines = [LivrosInline]
