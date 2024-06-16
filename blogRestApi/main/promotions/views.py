from rest_framework import viewsets
from rest_framework import permissions

from main.promotions.models import Promotion
from main.promotions.serializers import PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Create your views here.
# from django.contrib.auth.models import Group
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from classes.serializers import ClasseSerializer, FiliereSerializer, PromotionSerializer
# from .models import Eleve

# User = get_user_model()


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


# class EleveSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Eleve
#         fields = ['url', 'id', 'user', 'filiere', 'classe', 'promotion']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         user_representation = {
#             'id': instance.user.id,
#             'username': instance.user.username,
#             'email': instance.user.email,
#             # Ajoutez d'autres champs de l'utilisateur que vous souhaitez afficher
#         }
#         representation['user'] = user_representation

#         if instance.classe:
#             classe_representation = {
#                 'id': instance.classe.id,
#                 'code': instance.classe.code,
#                 # Ajoutez d'autres champs de la classe que vous souhaitez afficher
#             }
#             representation['classe'] = classe_representation
#         else:
#             representation['classe'] = None

#         filiere_representation = {
#             'id': instance.filiere.id,
#             'codeFiliere': instance.filiere.codeFiliere,
#             # Ajoutez d'autres champs de la filière que vous souhaitez afficher
#         }
#         representation['filiere'] = filiere_representation

#         if instance.promotion:
#             promotion_representation = {
#                 'id': instance.promotion.id,
#                 'anneeDebut': instance.promotion.anneeDebut,
#                 'anneeFin': instance.promotion.anneeFin,
#                 # Ajoutez d'autres champs de la promotion que vous souhaitez afficher
#             }
#             representation['promotion'] = promotion_representation
#         else:
#             representation['promotion'] = None

#         return representation

#     def create(self, validated_data):
#         eleve = Eleve.objects.create(**validated_data)
#         group = Group.objects.get(name='Student')
#         eleve.user.groups.add(group)
#         return eleve
