from django.shortcuts import render
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema
from accounts.models import CustomUser
from accounts.serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class RegisterAPI(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class LoginAPI(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        data = request.data
        user = authenticate(request, username=data.get('email'), password=data.get('password'))
        user_verify = CustomUser.objects.filter(email=data.get('email')).first()
        if user and user_verify.verified:
            refresh = RefreshToken.for_user(user)
            return Response({'email': user.email, 'name': user.name, 'refresh': str(refresh),
                             'access': str(refresh.access_token), 'verified': True},
                            status=status.HTTP_200_OK)
        elif user:
            return Response({'auth_token': '', 'user': user_verify.name, 'verified': False})
        else:
            return Response('user not found', status=status.HTTP_401_UNAUTHORIZED)
