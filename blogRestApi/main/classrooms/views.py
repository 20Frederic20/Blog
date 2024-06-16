from rest_framework import viewsets
from rest_framework import permissions

from main.promotions.models import Classroom
from main.promotions.serializers import ClassroomSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    permission_classes = [permissions.IsAuthenticated]
