from rest_framework import serializers
from .models import *
from app.user.serializers import UserSerializers


class AuthorNewsSerializers(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author_username",
            "created_at",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def get_author_username(self, obj):
        return obj.author.username


class NewsSerializers(serializers.ModelSerializer):
    author = UserSerializers()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "author",
            "created_at",
            "news_comments",
            "like_count",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }

    def get_author_username(self, obj):
        return obj.author.username

    def get_like_count(self, obj):
        return obj.like_set.count()