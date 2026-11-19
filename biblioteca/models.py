from django.db import models

from .validators import FileExtensionValidator, validate_isbn, validate_number_of_pages, validate_size_of_file, validate_year

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Authors"
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name='books_tmp', blank=True)
    category = models.ManyToManyField(Category, blank=True)
    year = models.IntegerField(validators=[validate_year])
    available = models.BooleanField(default=True)
    paginas = models.IntegerField(null=True, blank=True, validators=[validate_number_of_pages])
    isbn = models.CharField(max_length=13, null=True, blank=True, validators=[validate_isbn])
    capa = models.ImageField(upload_to='book_covers/', null=True, blank=True, validators=[FileExtensionValidator, validate_size_of_file])

    def __str__(self):
        return f"{self.title} - {self.year} - {'Disponível' if self.available else 'Indisponível'}"