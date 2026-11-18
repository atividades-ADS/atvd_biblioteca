from django import forms
from .models import Livro
from django.utils import timezone

class AuthorForm(forms.Form):
    name = forms.CharField(label="Nome:", max_length=100, required=True)
    nationality = forms.CharField(label="Nacionalidade:",max_length=100, required=False)

class LivroModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["capa", "titulo", "authors", "ano_publicacao", "disponivel", "categories", "paginas", "isbn"]
        labels = {"capa": "Capa","titulo": "Título", "authors": "Autores", "ano_publicacao": "Ano de publicação", "disponivel": "Disponível?", "categories": "Categorias", "paginas": "Número de páginas", "isbn": "ISBN"}
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'capa': forms.ClearableFileInput(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if (len(titulo) < 3):
            raise forms.ValidationError("O título deve ter pelo menos 3 caracteres.")
        return titulo

    def clean_ano_publicacao(self):
        ano = self.cleaned_data["ano_publicacao"]
        agora = timezone.now()

        if (ano > agora.year):
            raise forms.ValidationError(f"O ano deve ser no máximo {agora.year}.")
        return ano

