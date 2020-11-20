from django.shortcuts import render

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Get all the posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Retrieving, updating and destroying a post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
