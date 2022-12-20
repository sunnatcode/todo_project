from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_app.exceptions import PasswordDidNotMatchException, UsernameTakenException, AlreadyTakenException


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.filter(user=user).first()
        if token:
            token.delete()
        token = Token(user=user)
        token.save()
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

    def permission_denied(self, request, message=None, code=None):
        return super().permission_denied(request, message, code)

    def get_exception_handler_context(self):
        return {
            "message": "Could not perform this action",
            "status": status.HTTP_403_FORBIDDEN
        }


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token = request.auth
        if token:
            token.delete()
        return Response({"message": "Logged out", "status": status.HTTP_200_OK})

    def permission_denied(self, request, message=None, code=None):
        return super().permission_denied(request, message, code)


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    model = User

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username")
        if User.objects.filter(username=username).exists():
            raise AlreadyTakenException("Username", 455)

        password: str = data.get("password")
        confirm_password: str = data.get("confirm_password")
        if not password.__eq__(confirm_password):
            raise PasswordDidNotMatchException()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        if User.objects.filter(email=email).exists():
            raise AlreadyTakenException("Email", 460)

        user = User(username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email)
        user.set_password(password)
        user.save()

        return Response({
            "message": "Successfully",
            "status": status.HTTP_200_OK,
            "user_id": user.id})
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        ser = RegisterSerializer(queryset, many=True)
        return Response(ser.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        refresh = RefreshToken.for_user(user)
        token = {
            "username": user.username,
            "smile": "✔✔✔",
            "ref": str(refresh),
            "acc": str(refresh.access_token),
        }
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
