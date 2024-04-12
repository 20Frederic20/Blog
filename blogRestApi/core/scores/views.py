from rest_framework import viewsets
from rest_framework import permissions

from core.promotions.models import Score
from core.promotions.serializers import ScoreSerializer



class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]
