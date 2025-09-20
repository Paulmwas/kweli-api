from django.urls import path

from .views import ArticleListView, ArticleDetailView, CategoryListView,CategoryArticlesView, TagListView, TagArticlesView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryArticlesView.as_view(), name='category-articles'),
    path('tags/<slug:slug>/', TagArticlesView.as_view(), name='category-articles'),
    path('tags/', TagListView.as_view(), name='category-list'),
]
