from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class BlogCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = Comments.objects.filter(blog_id=obj.id)
        return CommentsSerializer(comments, many=True).data

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'body', 'posted', 'category', 'enable', 'comments']
