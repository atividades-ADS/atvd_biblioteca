from django.contrib import admin
from .models import Livro, Author, Category

# Register your models here.

admin.site.register(Category)
class CategoriesInline(admin.TabularInline):
    model = Category
    extra = 1

admin.site.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "author", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "author", ]
    list_filter = ["disponivel", "categories"]
    filter_horizontal = ["categories"]

admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline]
