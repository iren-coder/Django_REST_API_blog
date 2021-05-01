from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from app.serializers import PostSerializer, CategorySerializer
from app.models import Post, Category


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
