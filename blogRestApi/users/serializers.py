from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from classes.serializers import ClasseSerializer, FiliereSerializer, PromotionSerializer
from .models import Eleve

User = get_user_model()



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password']


class EleveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eleve
        fields = ['url', 'id', 'user', 'filiere', 'classe', 'promotion']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = {
            'id': instance.user.id,
            'username': instance.user.username,
            'email': instance.user.email,
            # Ajoutez d'autres champs de l'utilisateur que vous souhaitez afficher
        }
        representation['user'] = user_representation

        if instance.classe:
            classe_representation = {
                'id': instance.classe.id,
                'codeClasse': instance.classe.codeClasse,
                # Ajoutez d'autres champs de la classe que vous souhaitez afficher
            }
            representation['classe'] = classe_representation
        else:
            representation['classe'] = None

        filiere_representation = {
            'id': instance.filiere.id,
            'codeFiliere': instance.filiere.codeFiliere,
            # Ajoutez d'autres champs de la filière que vous souhaitez afficher
        }
        representation['filiere'] = filiere_representation

        if instance.promotion:
            promotion_representation = {
                'id': instance.promotion.id,
                'anneeDebut': instance.promotion.anneeDebut,
                'anneeFin': instance.promotion.anneeFin,
                # Ajoutez d'autres champs de la promotion que vous souhaitez afficher
            }
            representation['promotion'] = promotion_representation
        else:
            representation['promotion'] = None

        return representation
