from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from blog.serializers import BlogDetailSerializer
from django_fsm import TransitionNotAllowed
from blog.models import BlogEntry, BlogEntryStates
from rest_framework import status


@api_view(http_method_names=["POST"])
@extend_schema(responses=BlogDetailSerializer)
@permission_classes([IsAuthenticated])
def publish(request: HttpRequest, pk: int = None) -> Response:
    blog_entry = get_object_or_404(BlogEntry.objects.filter(id=pk))
    if blog_entry.created_by != request.user:
        return Response("Forbidden", status=status.HTTP_403_FORBIDDEN)
    try:
        blog_entry.publish()
    except TransitionNotAllowed as err:
        current_state = BlogEntryStates(blog_entry.state).name
        desired_state = BlogEntryStates.PUBLISHED.name
        return Response(
            f"Transition from {current_state} to {desired_state} not allowed",
            status=status.HTTP_412_PRECONDITION_FAILED,
        )
    blog_entry.save()
    return Response(BlogDetailSerializer(blog_entry).data, status=status.HTTP_200_OK)


@api_view(http_method_names=["POST"])
@extend_schema(responses=BlogDetailSerializer)
@permission_classes([IsAuthenticated])
def archive(request: HttpRequest, pk: int = None) -> Response:
    blog_entry = get_object_or_404(BlogEntry.objects.filter(id=pk))
    if blog_entry.created_by != request.user:
        return Response("Forbidden", status=status.HTTP_403_FORBIDDEN)
    try:
        blog_entry.publish()
    except TransitionNotAllowed as err:
        current_state = BlogEntryStates(blog_entry.state).name
        desired_state = BlogEntryStates.PUBLISHED.name
        return Response(
            f"Transition from {current_state} to {desired_state} not allowed",
            status=status.HTTP_412_PRECONDITION_FAILED,
        )
    blog_entry.save()
    return Response(BlogDetailSerializer(blog_entry).data, status=status.HTTP_200_OK)
