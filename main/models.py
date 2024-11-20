from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    biography = models.TextField()
    book_count = models.PositiveIntegerField(default=0)


class Book(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()