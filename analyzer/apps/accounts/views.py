from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class SignupView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response(
                data={"message": "User created successfully", "user": user_serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(data={"message": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
