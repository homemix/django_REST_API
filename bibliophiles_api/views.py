from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

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

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class GenreSerializer(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewSerializer(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
