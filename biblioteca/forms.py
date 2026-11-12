from django import forms
from .models import Author, Category, Book

import datetime


class AuthorForm(forms.Form):
    name = forms.CharField(
        label="Nome do autor",
        max_length=100,
        required=True
    )
    nationality = forms.CharField(label="Nacionalidade", required=False)
    
    def clean(self):

        cleaned_data = super().clean()

        nationality = cleaned_data.get("nationality")

       
        if nationality and len(nationality) > 50:
            self.add_error("nationality", "Esté campo aceita até 50 caracteres.")

        return cleaned_data


class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ["name"]


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, label="Titulo")
    author = forms.ModelMultipleChoiceField(
        label="Autores",
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # ou forms.SelectMultiple
        required=True,
    )
    category = forms.ModelMultipleChoiceField(
        label="Categoria",
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # ou forms.SelectMultiple
        required=True,
    )
    year = forms.IntegerField(label="Ano de publicação")
    available = forms.BooleanField(label="Disponível")



class BookModelForm(forms.ModelForm):
    
    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 3:
            raise forms.ValidationError("O titulo deve ter pelo menos 3 caracteres!")
        return title
            
    def clean_year(self):
        year = self.cleaned_data["year"]
        if year > datetime.date.today().year:
            raise forms.ValidationError("O ano não pode ser posterior ao ano atual")
        return year
        

    class Meta: 
        model = Book
        fields = "__all__"
        widgets = {
            "category": forms.CheckboxSelectMultiple,
            "authors": forms.CheckboxSelectMultiple,
        }