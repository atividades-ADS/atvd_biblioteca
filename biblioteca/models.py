from django.db import models

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
    year = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.year} - {'Disponível' if self.available else 'Indisponível'}"