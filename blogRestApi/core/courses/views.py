from rest_framework import viewsets
from rest_framework import permissions

from core.promotions.models import Course
from core.promotions.serializers import CourseSerializer



class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
