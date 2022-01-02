from django.shortcuts import render
from accounts import serializers
from blog.models import BlogEntry
from rest_framework import generics
from blog.serializers import BlogDetailSerializer, BlogListSerializer, BlogCreateSerializer

class ListBlogEntries(generics.ListAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogListSerializer

class RetrieveBlogEntry(generics.RetrieveAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogDetailSerializer

class CreateBlogEntry(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
