from rest_framework import viewsets
from rest_framework import permissions

from main.promotions.models import Subject
from main.promotions.serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]
