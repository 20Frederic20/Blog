from rest_framework import viewsets, views, status, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import  Group
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, GroupSerializer, EleveSerializer
from .models import Eleve
from classes.models import Classe, Promotion, Filiere

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class EleveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Eleves to be viewed or edited.
    """
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filiere_id = self.request.GET.get('filiere_id')
        classe_id = self.request.GET.get('classe_id')
        if filiere_id and classe_id:
            return Eleve.objects.filter(filiere__id=filiere_id, classe__id=classe_id)
        if filiere_id:
            return Eleve.objects.filter(filiere__id=filiere_id)
        if classe_id:
            return Eleve.objects.filter(classe__id=classe_id)
        return Eleve.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username
        })


class LogoutView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
