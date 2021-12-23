from django.core.exceptions import ValidationError
from rest_framework import serializers

from blog.models import BlogEntry

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "title",
            "updated_at"
        ]

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "title",
            "content",
            "created_by",
        ]

    def create(self, validated_data):
        return BlogEntry.objects.create(**validated_data) 