from django import forms
from .models import Author, Category, Book


class AuthorForm(forms.Form):
    name = forms.CharField(
        label="Nome do autor",
        max_length=100,
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Selecione uma categoria"
    )


class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ["name"]


class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ["title", "authors", "category"]
