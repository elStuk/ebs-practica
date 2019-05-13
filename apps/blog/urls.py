from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogRegisterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('create_blog/', BlogRegisterView.as_view(), name="create_blog"),
]
