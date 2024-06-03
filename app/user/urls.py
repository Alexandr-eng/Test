from django.urls import path

from app.user.views import UserView, UserCreate

urlpatterns = [
    path("user/", UserView.as_view({"get": "retrieve", "put": "update"})),
    path("registration/", UserCreate.as_view({"post": "create"})),
]