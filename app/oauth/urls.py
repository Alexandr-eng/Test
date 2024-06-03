from django.urls import path

from app.oauth.views import TokenView

urlpatterns = [
    path("auth/", TokenView.as_view(), name="auth"),
]