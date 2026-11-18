from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, FileExtensionValidator
from .validators import validate_file_size
from django.utils import timezone



class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, null=True, blank=True)

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
    capa = models.ImageField(upload_to="capas/", blank=True, null=True, validators=[
        validate_file_size,
        FileExtensionValidator(["jpg", "jpeg", "png"]),
    ])
    titulo = models.CharField(
        max_length=100,
        validators=[
        MinLengthValidator(3)
        ],
    )
    ano_publicacao = models.IntegerField(
        validators=[
            MinValueValidator(1450),
            MaxValueValidator(timezone.now().year),
        ]
    )
    paginas = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5000),
        ],
    )
    isbn = models.CharField(null=True, blank=True, max_length=13, validators=[
        MinLengthValidator(13),
    ])
    disponivel = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.ano_publicacao} - {'Disponível' if self.disponivel else 'Indisponível'}"
