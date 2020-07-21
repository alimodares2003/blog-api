from rest_framework import viewsets
from blog import serializers
from rest_framework import permissions
from core.models import Post, Category, Tag
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from blog import paginations


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'content',)
    ordering_fields = '__all__'
    pagination_class = paginations.PostNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = '__all__'

    @action(methods=['get'], detail=True, permission_classes=[permissions.AllowAny])
    def posts(self, request, pk=None):
        category = Category.objects.get(id=pk)
        posts = Post.objects.filter(category_id=category)
        post_serializer = serializers.PostSerializer(posts, many=True)
        return Response(post_serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = '__all__'

    @action(methods=['get'], detail=True, permission_classes=[permissions.AllowAny])
    def posts(self, request, pk=None):
        tag = Tag.objects.get(id=pk)
        posts = Post.objects.filter(tag=tag)
        post_serializer = serializers.PostSerializer(posts, many=True)
        return Response(post_serializer.data)
