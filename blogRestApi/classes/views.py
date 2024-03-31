from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Coefficient, Filiere
from users.models import Note
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

    # def get_queryset(self):
    #     filiere_id = self.request.GET.get('filiere_id')
    #     classe_id = self.request.GET.get('classe_id')
    #     if filiere_id and classe_id:
    #         return Matiere.objects.filter(filiereMatiere__id=filiere_id, classeMatiere__id=classe_id)
    #     if classe_id:
    #         return Matiere.objects.filter(classeMatiere__id=classe_id)
    #     return Matiere.objects.all()  # Renvoyer une liste vide si aucun ID de classe n'est fourni
    
    def get_queryset(self):
        eleve = self.request.GET.get('eleve', None)
        if eleve:
            coefficients = Coefficient.objects.filter(classe=eleve.classe, filiere=eleve.filiere)
            if coefficients:
                matieres_representation = []
                for coefficient in coefficients:
                    matiere_representation = {
                        'id': coefficient.matiere.id,
                        'codeMatiere': coefficient.matiere.codeMatiere,
                        'denomination': coefficient.matiere.denomination,
                    }
                    matieres_representation.append(matiere_representation)
            return matieres_representation
        return Matiere.objects.all()


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