from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.nationality}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name}"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.ano_publicacao} - {'Disponível' if self.disponivel else 'Indisponível'}"