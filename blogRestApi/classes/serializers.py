from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Note, Coefficient, Filiere
from rest_framework import serializers


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ['url', 'id', 'codeFiliere', 'nomFiliere']


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['url', 'id', 'codeClasse', 'libelleClasse',]


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['url', 'id', 'anneeDebut', 'anneeFin']


class TrimestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trimestre
        fields = ['url', 'id', 'codeTrimestre']


class DevoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devoir
        fields = ['url', 'id', 'codeDevoir',
                  'typeDevoir', 'denominationDevoir']


class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = ['url', 'id', 'codeMatiere', 'denomination',
                  'classeMatiere', 'filiereMatiere', 'appreciation']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.classeMatiere:
            classeMatiere_representation = {
                'id': instance.classeMatiere.values_list('id', flat=True),
                'codeClasse': instance.classeMatiere.values_list('codeClasse', flat=True),
                'libelleClasse': instance.classeMatiere.values_list('libelleClasse', flat=True),
            }
        else:
            classeMatiere_representation = None  # or any other default representation

        representation['classeMatiere'] = classeMatiere_representation

        if instance.filiereMatiere:
            filiereMatiere_representation = {
                'id': instance.filiereMatiere.values_list('id', flat=True),
                'codeFiliere': instance.filiereMatiere.values_list('codeFiliere', flat=True),
                # Ajoutez d'autres champs de la filière que vous souhaitez afficher
            }
            representation['filiereMatiere'] = filiereMatiere_representation

        return representation


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['url', 'id', 'devoirNote', 'eleve',
                  'matiereNote', 'valeurNote', 'trimestreDevoir',]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.devoirNote:
            devoirNote_representation = {
                'id': instance.devoirNote.id,
                'codeDevoir': instance.devoirNote.codeDevoir,
                'typeDevoir': instance.devoirNote.typeDevoir,
                'denominationDevoir': instance.devoirNote.denominationDevoir,
            }
            representation['devoirNote'] = devoirNote_representation

        eleve_representation = {
            'id': instance.eleve.id,
            'username': instance.eleve.user.username,
        }
        representation['eleve'] = eleve_representation

        matieres_queryset = Matiere.objects.filter(
            classeMatiere=instance.eleve.classe)

        if matieres_queryset:
            matieres_representation = []
            for matiere in matieres_queryset:
                matiere_representation = {
                    'id': matiere.id,
                    'codeMatiere': matiere.codeMatiere,
                    'denomination': matiere.denomination,
                }
                matieres_representation.append(matiere_representation)

            representation['matieres'] = matieres_representation

        if instance.matiereNote:
            matiereNote_representation = {
                'id': instance.matiereNote.id,
                'codeMatiere': instance.matiereNote.codeMatiere,
                'denomination': instance.matiereNote.denomination,
            }
        else:
            matiereNote_representation = None  # or any other default representation

        representation['matiereNote'] = matiereNote_representation

        if instance.trimestreDevoir:
            trimestreDevoir_representation = {
                'id': instance.trimestreDevoir.id,
                'codeTrimestre': instance.trimestreDevoir.codeTrimestre,
            }
            representation['trimestreDevoir'] = trimestreDevoir_representation

        return representation


class CoefficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coefficient
        fields = ['url', 'matiereCoefficient',
                  'filiereCoefficient', 'valeurCoefficient']
