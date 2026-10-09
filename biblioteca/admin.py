from django.contrib import admin
from .models import Author, Category, Book

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    search_fields = ('name', 'nationality')
    editable_fields = ('name', 'nationality')
    inlines = [BookInline]
    
    
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'year', 'available')
    list_filter = ('available', 'category',)
    search_fields = ('title', 'author__name', )
    filter_horizontal = ('category',)
admin.site.register(Book, BookAdmin)


admin.site.register(Category)
