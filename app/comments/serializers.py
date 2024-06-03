from rest_framework import serializers
from .models import CommentModel
from app.user.serializers import UserSerializers


class AuthorCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "text",
            "created_at",
            "author",
            "news",
        )
        extra_kwargs = {
            "author": {"read_only": True},
            "created_at": {"read_only": True},
        }


class CommentSerializers(serializers.ModelSerializer):
    author = UserSerializers()

    class Meta:
        model = CommentModel
        fields = (
            "id",
            "text",
            "created_at",
            "author",
            "news",
        )