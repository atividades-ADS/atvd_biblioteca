from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    nationality = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "authors"

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    author = models.ForeignKey(Author, related_name="books", null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.titulo} - {self.ano_publicacao} - {'Disponível' if self.disponivel else 'Indisponível'}"