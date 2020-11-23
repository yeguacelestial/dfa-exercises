from django.shortcuts import render

from rest_framework import generics, permissions  # new
from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly  # new
from .serializers import PostSerializer


# Get all the posts
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Retrieving, updating and destroying a post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
