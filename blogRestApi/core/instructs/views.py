from rest_framework import viewsets
from rest_framework import permissions

from core.promotions.models import Instruct
from core.promotions.serializers import InstructSerializer



class InstructViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Instruct.objects.all()
    serializer_class = InstructSerializer
    permission_classes = [permissions.IsAuthenticated]
