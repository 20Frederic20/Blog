from rest_framework import viewsets
from rest_framework import permissions

from core.promotions.models import Register
from core.promotions.serializers import RegisterSerializer



class RegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]
