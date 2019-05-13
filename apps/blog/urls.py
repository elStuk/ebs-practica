from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogRegisterView, CommentsListView, \
    CommentsRegisterView, CommentItemView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('create_blog/', BlogRegisterView.as_view(), name='create_blog'),
    path('comments_blog/', CommentsListView.as_view(), name='comments_blog'),
    path('create_comments_blog/', CommentsRegisterView.as_view(), name='create_comments_blog'),
    path('comments/<int:pk>/', CommentItemView.as_view(), name='comment_item'),

]
