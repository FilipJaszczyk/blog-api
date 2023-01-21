from blog.models import BlogEntry, BlogEntryStates
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    BlogCreateSerializer,
)


class ListBlogEntries(generics.ListAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogListSerializer


class RetrieveBlogEntry(generics.RetrieveAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogDetailSerializer


class CreateBlogEntry(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]
