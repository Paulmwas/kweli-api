from rest_framework import generics, permissions
from .models import Article, Category, Tag
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CategorySerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(status='published').order_by('-publish_date')
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryArticlesView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    
    def get_queryset(self):
        category_slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=category_slug)
        return Article.objects.filter(
            category=category,
            status='published'
        ).order_by('-publish_date')
    
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class TagArticlesView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    
    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag = get_object_or_404(Category, slug=tag_slug)
        return Article.objects.filter(
            tag=tag,
            status='published'
        ).order_by('-publish_date')