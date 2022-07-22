from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    genre = models.OneToOneField(
        Genre,
        on_delete=models.CASCADE,
        related_name='book'
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField()
    review = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='review'
    )
