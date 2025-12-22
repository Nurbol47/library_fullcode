from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookView(generics.ListCreateAPIView):
    queryser = Book.objects.all()
    serializer_class = BookSerializer
