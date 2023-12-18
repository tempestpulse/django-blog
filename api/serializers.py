from rest_framework import serializers
from core.models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
