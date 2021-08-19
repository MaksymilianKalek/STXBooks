from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

from .serializers import BookSerializer, AuthorSerializer, CategorySerializer
from .models import Book, Author, Category

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        authors = self.request.query_params.getlist('author')
        published_date = self.request.query_params.get('published_date')
        sort = self.request.query_params.get('sort')
        if published_date is not None and published_date != '':
            queryset = queryset.filter(published_date=published_date)
        if authors is not None and len(authors) > 0:
            authors_list = []
            for author in authors:
                author = author.replace('"', '')
                a = Author.objects.get(author=author)
                authors_list.append(a)
            queryset = queryset.filter(authors__in=authors_list)
        if sort is not None and sort != '':
            queryset = queryset.order_by(sort)
        return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DBPost(APIView):

    def post(self, request, format=None):
        URL = 'https://www.googleapis.com/books/v1/volumes'
        params = {'q': 'war'}
        r_json = requests.get(url=URL, params=params).json()
        all_books = Book.objects.all()
        all_authors = Author.objects.all()
        all_categories = Category.objects.all()
        for book in r_json['items']:
            title = book['volumeInfo']['title']
            if len(all_books.filter(title=title)) != 0:
                b = all_books.get(title=title)
            else:
                b = Book(title=title)

            if 'publishedDate' in book['volumeInfo']:
                b.published_date = book['volumeInfo']['publishedDate']

            if 'averageRating' in book['volumeInfo']:
                b.average_rating = float(
                    book['volumeInfo']['averageRating'])
            if 'ratingsCount' in book['volumeInfo']:
                b.ratings_count = int(book['volumeInfo']['ratingsCount'])
            if 'imageLinks' in book['volumeInfo'] and 'thumbnail' in book['volumeInfo']['imageLinks']:
                b.thumbnail = book['volumeInfo']['imageLinks']['thumbnail']
            b.save()
            if 'authors' in book['volumeInfo']:
                for author in list(book['volumeInfo']['authors']):
                    if len(all_authors.filter(author=author)) == 0:
                        b.authors.create(author=author)
                    else:
                        b.authors.add(all_authors.get(author=author))
                b.save()
            if 'categories' in book['volumeInfo']:
                for category in list(book['volumeInfo']['categories']):
                    if len(all_categories.filter(category=category)) == 0:
                        b.categories.create(category=category)
                    else:
                        b.categories.add(
                            all_categories.get(category=category))
                b.save()

        return Response(status=status.HTTP_201_CREATED)
