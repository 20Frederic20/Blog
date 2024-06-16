from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from main.promotions.models import Register
from main.promotions.serializers import RegisterSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        classroom_id = self.request.GET.get("classroom_id", None)
        promotion_id = self.request.GET.get("promotion_id", None)

        queryset = Register.objects.all()

        if classroom_id:
            queryset = queryset.filter(classroom=classroom_id)

        if promotion_id:
            queryset = queryset.filter(promotion=promotion_id)

        return queryset
