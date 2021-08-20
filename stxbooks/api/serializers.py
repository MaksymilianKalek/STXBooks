from rest_framework import serializers

from .models import Book, Author, Category


class AuthorSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        return obj.author

    class Meta:
        model = Author
        fields = ['author']


class CategorySerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        return obj.category

    class Meta:
        model = Category
        fields = ['category']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ['title', 'authors', 'published_date',
                  'categories', 'average_rating', 'ratings_count', 'thumbnail']
