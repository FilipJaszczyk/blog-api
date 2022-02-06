from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiResponse, extend_schema
from django_fsm import TransitionNotAllowed
from rest_framework import status
from blog.models import BlogEntry, BlogEntryStates
from rest_framework import generics
from blog.serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    BlogCreateSerializer,
)
# TODO: move views to separate files under views/dir
# TODO: add integration tests for blog model related views


class ListBlogEntries(generics.ListAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogListSerializer


class RetrieveBlogEntry(generics.RetrieveAPIView):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogDetailSerializer


class CreateBlogEntry(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer

@api_view(http_method_names=["POST"])
@extend_schema(responses=BlogDetailSerializer)
@permission_classes([IsAuthenticated])
def archive(request: HttpRequest, pk: int = None) -> Response:
    blog_entry = get_object_or_404(BlogEntry.objects.filter(id=pk))
    try:
        blog_entry.publish()
    except TransitionNotAllowed as err:
        current_state = BlogEntryStates(blog_entry.state).name
        desired_state = BlogEntryStates.PUBLISHED.name
        return Response(f"Transition from {current_state} to {desired_state} not allowed", status=status.HTTP_412_PRECONDITION_FAILED)
    blog_entry.save()
    return Response(BlogDetailSerializer(blog_entry), status=status.HTTP_200_OK)
    
@api_view(http_method_names=["POST"])
@extend_schema(responses=BlogDetailSerializer)
@permission_classes([IsAuthenticated])
def publish(request: HttpRequest, pk: int = None) -> Response:
    blog_entry = get_object_or_404(BlogEntry.objects.filter(id=pk))
    try:
        blog_entry.publish()
    except TransitionNotAllowed as err:
        current_state = BlogEntryStates(blog_entry.state).name
        desired_state = BlogEntryStates.PUBLISHED.name
        return Response(f"Transition from {current_state} to {desired_state} not allowed", status=status.HTTP_412_PRECONDITION_FAILED)
    blog_entry.save()
    return Response(BlogDetailSerializer(blog_entry), status=status.HTTP_200_OK)