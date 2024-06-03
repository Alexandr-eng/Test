from django.urls import path

from app.news.views import NewsAuthorViewSet, NewsViewSet

urlpatterns = [
    path(
        "my-news/", NewsAuthorViewSet.as_view({"get": "list", "post": "create"})
    ),
    path(
        "my-news/<int:pk>",
        NewsAuthorViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("", NewsViewSet.as_view({"get": "list"})),
    path("<int:pk>", NewsViewSet.as_view({"get": "retrieve"})),]