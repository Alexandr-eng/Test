from django.urls import path, include
from .schemas import schema_view


urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("user/", include("app.user.urls")),
    path("auth/", include("app.oauth.urls")),
    path("news/", include("app.news.urls")),
    path("comment/", include("app.comments.urls")),
    path("like/", include("app.likes.urls")),
]