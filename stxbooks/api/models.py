from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.PositiveIntegerField(default=0)
    categories = models.TextField(null=True)
    average_rating = models.FloatField()
    ratings_count = models.PositiveIntegerField()
    thumbnail = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.authors}"
