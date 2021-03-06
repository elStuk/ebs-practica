from drf_util.decorators import serialize_decorator
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.models import Category, Blog, Comments
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentsSerializer

"""
    Category
"""


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""
    COMMENTS
"""


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class CommentsListView(GenericAPIView):
    serializer_class = CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        comments = Comments.objects.all()

        return Response(CommentsSerializer(comments, many=True).data)


class CommentsRegisterView(GenericAPIView):
    serializer_class = CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentsSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comments = Comments.objects.create(
            title=validated_data['title'],
            blog=validated_data['blog'],
        )

        comments.save()

        return Response(CommentsSerializer(comments).data)


class CommentItemView(GenericAPIView):
    serializer_class = CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        comments = get_object_or_404(Comments.objects.filter(pk=pk))

        return Response(CommentsSerializer(comments).data)


"""
    BLOG
"""


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer, CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()

        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer, CommentsSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = Comments.objects.filter(blog_id=blog.id)

        blog_and_comments = BlogSerializer(blog).data.copy()
        blog_and_comments.update({'comments': CommentsSerializer(comments, many=True).data})

        return Response(blog_and_comments)


class BlogRegisterView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            category=validated_data['category'],
            enable=validated_data['enable'],
        )

        blog.save()

        return Response(BlogSerializer(blog).data)
