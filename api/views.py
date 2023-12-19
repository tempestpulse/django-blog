from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, SAFE_METHODS

from core.models import Post, Category, Comment
from .serializers import PostSerializer, CategorySerializer, CommentSerializer


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to author'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

