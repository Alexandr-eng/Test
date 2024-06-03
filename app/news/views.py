from rest_framework import viewsets, permissions

from . import serializers
from .models import News

from .permission import AdminOrAuthor
from .pagination import Pagination


class NewsAuthorViewSet(viewsets.ModelViewSet):


    permission_classes = [AdminOrAuthor]
    serializer_class = serializers.AuthorNewsSerializers

    def get_queryset(self):
        return News.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


class NewsViewSet(viewsets.ModelViewSet):


    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination

    def get_serializer_context(self):
        return {"request": self.request}

