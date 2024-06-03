from rest_framework import viewsets, permissions
from . import serializers




class UserCreate(viewsets.ModelViewSet):

    serializer_class = serializers.UserSerializers
    permissions_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UserView(viewsets.ModelViewSet):


    serializer_class = serializers.UserSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
