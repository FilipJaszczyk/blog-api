from rest_framework import serializers
from utils.serializers import ReadOnlyModelSerializer
from blog.models import BlogEntry


class BlogListSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ["id", "title", "updated_at"]


class BlogCreateSerializer(serializers.ModelSerializer):
    """
    Functionality relies on IsAuthenticated permission as it is
    extracting informations related to Account from `context["request"]`
    """
    class Meta:
        model = BlogEntry
        fields = [
            "title",
            "content",
        ]

    def create(self, validated_data):
        return BlogEntry.objects.create(**validated_data, 
        created_by=self.context["request"].user)


class BlogDetailSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ["title", "content", "created_at"]
