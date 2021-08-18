from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer
from .models import Book

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset
