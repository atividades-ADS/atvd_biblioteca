from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(label="Nome:", max_length=100, required=True)
    nationality = forms.CharField(label="Nacionalidade:",max_length=100, required=False)