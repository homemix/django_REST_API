from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .serializers import BookSerializer, GenreSerializer, ReviewSerializer
from .models import Book, Genre, Review


# Create your views here.
@swagger_auto_schema(tags=['Book Endpoint'])
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Books
    """
    queryset = Book.objects.all().order_by('published_date')
    serializer_class = BookSerializer


class GenreSerializer(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewSerializer(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
