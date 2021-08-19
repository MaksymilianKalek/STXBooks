from django.db import models

# Create your models here.


class Author(models.Model):
    author = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author}"


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    published_date = models.CharField(max_length=200, null=True)
    categories = models.ManyToManyField(Category)
    average_rating = models.FloatField(null=True)
    ratings_count = models.PositiveIntegerField(null=True)
    thumbnail = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f"{self.title} - {self.published_date}"
