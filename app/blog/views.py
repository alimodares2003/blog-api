from rest_framework import viewsets
from blog import serializers
from rest_framework import permissions
from core.models import Post, Category


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny,)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.AllowAny,)
