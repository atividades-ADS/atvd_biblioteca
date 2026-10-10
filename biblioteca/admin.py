from django.contrib import admin
from .models import Author, Category, Book

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    search_fields = ('name', 'nationality')
    editable_fields = ('name', 'nationality')
    
    
    
class BookAdmin(admin.ModelAdmin):
    
    def list_authors(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])
    list_authors.short_description = 'Autores'
    list_display = ('title', 'list_authors', 'year', 'available')
    list_filter = ('available', 'category',)
    search_fields = ('title', 'authors__name', )
    filter_horizontal = ('category','authors',)
    
admin.site.register(Book, BookAdmin)


admin.site.register(Category)
