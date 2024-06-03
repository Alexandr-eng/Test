from rest_framework import viewsets, permissions, status, exceptions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import serializers
from app.news.permission import AdminOrAuthor
from .models  import CommentModel
from app.news.pagination import Pagination


class ComentAuthorView(viewsets.ModelViewSet):


    serializer_class = serializers.AuthorCommentSerializers
    permission_classes = [AdminOrAuthor]

    def get_queryset(self):
        return CommentModel.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(viewsets.ModelViewSet):


    serializer_class = serializers.CommentSerializers
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Pagination

    def get_queryset(self):
        return CommentModel.objects.filter(news=self.kwargs.get("pk"))

    def get_object(self):
        comment = get_object_or_404(CommentModel, pk=self.kwargs["comment_pk"])
        if comment.news.author != self.request.user:
            raise exceptions.PermissionDenied(
                "You do not have permission to delete this comment."
            )
        self.check_object_permissions(self.request, comment)
        return comment

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        self.perform_destroy(comment)
        return Response(status=status.HTTP_204_NO_CONTENT)
