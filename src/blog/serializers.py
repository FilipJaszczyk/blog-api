from rest_framework import serializers
from utils.serializers import ReadOnlyModelSerializer
from blog.models import BlogEntry

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = [
            "id",
            "title",
            "updated_at"
        ]

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = [
            "title",
            "content",
            "created_by",
        ]

    def create(self, validated_data):
        return BlogEntry.objects.create(**validated_data) 

class BlogDetailSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = BlogEntry
        fields = [
            "title",
            "content",
            "created_at"
        ]