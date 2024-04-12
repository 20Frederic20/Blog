# from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Coefficient, Filiere
# from rest_framework import serializers
# from users.models import Note


# class FiliereSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Filiere
#         fields = ['url', 'id', 'codeFiliere', 'nomFiliere']


# class ClasseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classe
#         fields = ['url', 'id', 'code', 'libelle',]


# class PromotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Promotion
#         fields = ['url', 'id', 'anneeDebut', 'anneeFin']


# class TrimestreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trimestre
#         fields = ['url', 'id', 'codeTrimestre']


# class DevoirSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Devoir
#         fields = ['url', 'id', 'code', 'type', 'denomination']


# class MatiereSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Matiere
#         fields = ['url', 'id', 'codeMatiere', 'denomination', 'appreciation']


# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ['url', 'id', 'devoir', 'eleve', 'matiere', 'valeur', 'trimestre',]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if instance.devoir:
#             devoir_representation = {
#                 'id': instance.devoir.id,
#                 'code': instance.devoir.code,
#                 'type': instance.devoir.type,
#                 'denomination': instance.devoir.denomination,
#             }
#             representation['devoir'] = devoir_representation

#         eleve_representation = {
#             'id': instance.eleve.id,
#             'username': instance.eleve.user.username,
#         }
#         representation['eleve'] = eleve_representation
        
#         coefficients = Coefficient.objects.filter(classe=instance.eleve.classe, filiere=instance.eleve.filiere)
#         matieres_representation = []
#         for coefficient in coefficients:
#             matiere = coefficient.matiere
#             if instance.matiere == matiere:  # Ne pas inclure la matière de la note dans la liste
#                 continue

#             matiere_representation = {
#                 'id': matiere.id,
#                 'codeMatiere': matiere.codeMatiere,
#                 'denomination': matiere.denomination,
#             }
#             matieres_representation.append(matiere_representation)

#         representation['matieres'] = matieres_representation
        
#         if instance.matiere:
#             matiere_representation = {
#                 'id': instance.matiere.id,
#                 'codeMatiere': instance.matiere.codeMatiere,
#                 'denomination': instance.matiere.denomination,
#             }
#         else:
#             matiere_representation = None  # or any other default representation

#         representation['matiere'] = matiere_representation


#         if instance.trimestre:
#             trimestre_representation = {
#                 'id': instance.trimestre.id,
#                 'codeTrimestre': instance.trimestre.codeTrimestre,
#             }
#             representation['trimestre'] = trimestre_representation

#         return representation


# class CoefficientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coefficient
#         fields = ['url', 'matiere', 'valeur', 'classe', 'filiere']
        
#         def to_representation(self, instance):
#             representation = super().to_representation(instance)

#             if instance.classe:
#                 classe_representation = {
#                     'id': instance.classe.values_list('id', flat=True),
#                     'code': instance.classe.values_list('code', flat=True),
#                     'libelle': instance.classe.values_list('libelle', flat=True),
#                 }
#             else:
#                 classe_representation = None  # or any other default representation

#             representation['classe'] = classe_representation

#             if instance.filiere:
#                 filiere_representation = {
#                     'id': instance.filiere.values_list('id', flat=True),
#                     'codeFiliere': instance.filiere.values_list('codeFiliere', flat=True),
#                     # Ajoutez d'autres champs de la filière que vous souhaitez afficher
#                 }
#                 representation['filiere'] = filiere_representation
                
#             if instance.matiere:
#                 matiere_representation = {
#                     'id': instance.matiere.values_list('id', flat=True),
#                     'codeMatiere': instance.matiere.values_list('codeMatiere', flat=True),
#                     'denomination': instance.matiere.values_list('denomination', flat=True),
#                 }
#             else:
#                 matiere_representation = None  
#             representation['matiere'] = matiere_representation

#             return representation
        

