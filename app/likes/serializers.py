from rest_framework import serializers
from .models import Like


class LikeSerializers(serializers.Serializer):
    class Meta:
        model = Like
        fields = ["user", "news"]