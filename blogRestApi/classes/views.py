from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Note, Coefficient, Filiere
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClasseSerializer, PromotionSerializer, TrimestreSerializer, DevoirSerializer, MatiereSerializer, NoteSerializer, CoefficientSerializer, FiliereSerializer


class ClasseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class TrimestreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Trimestre.objects.all()
    serializer_class = TrimestreSerializer


class DevoirViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Devoir.objects.all()
    serializer_class = DevoirSerializer


class MatiereViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CoefficientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Coefficient.objects.all()
    serializer_class = CoefficientSerializer


class FiliereViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer