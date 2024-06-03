from rest_framework import status, views
from rest_framework.response import Response

from app.user.models import User

from drf_yasg.utils import swagger_auto_schema

from .oauths import create_token
from .serializers import TokenSerializers




class TokenView(views.APIView):
    @swagger_auto_schema(request_body=TokenSerializers, responses={200: "Token"})
    def post(self, request):
        try:
            user = User.objects.get(username=request.data.get("username"))
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token = create_token(user_id=user.id)
        return Response(token, status=status.HTTP_200_OK)