from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, GenreSerializer, ReviewSerializer
from .models import Book, Genre, Review


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('published_date')
    serializer_class = BookSerializer


class GenreSerializer(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewSerializer(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
