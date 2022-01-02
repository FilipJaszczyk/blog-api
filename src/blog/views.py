from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, extend_schema
from blog.models import BlogEntry
from rest_framework import generics
from blog.serializers import BlogDetailSerializer, BlogListSerializer, BlogCreateSerializer

class ListBlogEntries(generics.ListAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogListSerializer

class RetrieveBlogEntry(generics.RetrieveAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogDetailSerializer

@extend_schema(responses={
        201: OpenApiResponse(response=OpenApiTypes.NONE)})
class CreateBlogEntry(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
