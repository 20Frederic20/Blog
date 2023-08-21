from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Note, Coefficient, Filiere
from rest_framework import serializers


class FiliereSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filiere
        fields = ['url', 'id', 'codeFiliere', 'nomFiliere']


class ClasseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classe
        fields = ['url', 'id', 'codeClasse', 'libelleClasse',]


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ['url', 'id', 'anneeDebut', 'anneeFin']


class TrimestreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trimestre
        fields = ['url', 'codeTrimestre']


class DevoirSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devoir
        fields = ['url', 'codeDevoir', 'denominationDevoir', 'trimestreDevoir', 'dateDevoir']


class MatiereSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matiere
        fields = ['url', 'codeMatiere', 'denomination', 'appreciation']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['url','devoirNote', 'eleve', 'matiereNote', 'valeurNote']


class CoefficientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coefficient
        fields = ['url', 'matiereCoefficient', 'filiereCoefficient', 'valeurCoefficient']


