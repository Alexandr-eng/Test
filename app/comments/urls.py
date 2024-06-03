from django.urls import path
from .views import CommentView, ComentAuthorView

urlpatterns = [
    path(
        "my_comments/",
        ComentAuthorView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "my_comments/<int:pk>/",
        ComentAuthorView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path(
        "comments_news/<int:pk>/",
        CommentView.as_view({"get": "list"}),
    ),
    path(
        "comments_news/<int:pk>/<int:comment_pk>/delete/",
        CommentView.as_view({"delete": "destroy"}),
    ),
]