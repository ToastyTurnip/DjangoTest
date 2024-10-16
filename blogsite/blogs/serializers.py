from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BlogPost
        fields = ["title", "content", "author", "created_at"]