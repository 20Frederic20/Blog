from django.contrib.auth import get_user_model

from rest_framework import viewsets, status, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

import json

from main.promotions.models import User, Student, Teacher, Register, Instruct
from main.promotions.serializers import UserSerializer, StudentSerializer, TeacherSerializer, RegisterSerializer, InstructSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teachers to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstructViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instructs to be viewed or edited.
    """
    queryset = Instruct.objects.all()
    serializer_class = InstructSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Registers to be viewed or edited.
    """
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username
        })


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentbyUserIdViewSet(APIView):
    def get(self, request, user_id, *args, **kwargs):
        student = Student.objects.get(user_id=user_id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
