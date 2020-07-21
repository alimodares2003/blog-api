from django.urls import path, include, reverse
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)

app_name = 'blog'

urlpatterns = [
    # path('categories/<int:pk>/post', views.CategoryViewSet.as_view({'get': 'get_posts'})),
    path('', include(router.urls)),
]
