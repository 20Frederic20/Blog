from rest_framework import viewsets
from rest_framework import permissions

from main.promotions.models import Coefficient
from main.promotions.serializers import CoefficientSerializer


class CoefficientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Coefficient.objects.all()
    serializer_class = CoefficientSerializer
    permission_classes = [permissions.IsAuthenticated]
