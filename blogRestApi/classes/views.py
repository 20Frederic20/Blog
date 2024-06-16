# from .models import Classe, Promotion, Trimestre, Devoir, Matiere, Coefficient, Filiere
# from users.models import Note
# from users.models import User, Eleve
# from .serializers import ClasseSerializer, PromotionSerializer, TrimestreSerializer, DevoirSerializer, MatiereSerializer, NoteSerializer, CoefficientSerializer, FiliereSerializer

# from rest_framework import viewsets, status, response, exceptions
# import json
# from rest_framework import permissions
# from rest_framework.views import APIView



# class ClasseViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Classe.objects.all()
#     serializer_class = ClasseSerializer


# class PromotionViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Promotion.objects.all()
#     serializer_class = PromotionSerializer


# class TrimestreViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Trimestre.objects.all()
#     serializer_class = TrimestreSerializer


# class DevoirViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Devoir.objects.all()
#     serializer_class = DevoirSerializer


# class MatiereViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Matiere.objects.all()
#     serializer_class = MatiereSerializer

#     # def get_queryset(self):
#     #     filiere_id = self.request.GET.get('filiere_id')
#     #     classe_id = self.request.GET.get('classe_id')
#     #     if filiere_id and classe_id:
#     #         return Matiere.objects.filter(filiereMatiere__id=filiere_id, classeMatiere__id=classe_id)
#     #     if classe_id:
#     #         return Matiere.objects.filter(classeMatiere__id=classe_id)
#     #     return Matiere.objects.all()  # Renvoyer une liste vide si aucun ID de classe n'est fourni
    
#     def get_queryset(self):
#         matieres_representation = []
#         filiere_id = self.request.GET.get('filiere_id', None)
#         classe_id = self.request.GET.get('classe_id', None)
        
#         if filiere_id and classe_id:
#             coefficients = Coefficient.objects.filter(classe__id=classe_id, filiere__id=filiere_id)
#             if coefficients:
#                 for coefficient in coefficients:
#                     matiere = Matiere.objects.filter(id=coefficient.matiere.id).first()
#                     matieres_representation.append(matiere)
#         if matieres_representation:
#             return matieres_representation
#         return Matiere.objects.all()


# class NoteViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


# class CoefficientViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Coefficient.objects.all()
#     serializer_class = CoefficientSerializer


# class FiliereViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Filiere.objects.all()
#     serializer_class = FiliereSerializer
    

# class CalculationsView(APIView):
#     def post(self, request, eleve_id, format=None):
#         try:
#             eleve = Eleve.objects.get(id=eleve_id)
#             coefficient = Coefficient.objects.filter(classe=eleve.classe, filiere=eleve.filiere)
#             coefficient_value, notes_interrogation, notes_devoir = [], [], []
            
#             if coefficient:
#                 for coef in coefficient:
#                     tableau = []  # Réinitialiser la liste à chaque itération
#                     notes = Note.objects.filter(eleve=eleve, matiere=coef.matiere)
#                     if notes.exists():
#                         notes_interrogation = [note.valeur for note in notes if "Interrogation" in note.devoir.denomination]
#                         notes_devoir = [note.valeur for note in notes if "Devoir" in note.devoir.denomination]# Vérifier s'il y a des notes associées
#                         for note in notes:
#                             petit = {
#                                 'note': note.valeur,
#                                 'devoir': note.devoir.denomination,
#                             }
#                             tableau.append(petit)
#                         notes_matieres = {
#                             'notes': tableau,
#                             'coefficient_value': coef.valeur,
#                             'matiere': coef.matiere.denomination
#                         }
#                         coefficient_value.append(notes_matieres) 
#             else:
#                 coefficient_value = 1 # Valeur par défaut si aucun coefficient n'est trouvé
#             moyenne_interro = sum(notes_interrogation) / len(notes_interrogation)
#             moyenne_devoir = sum(notes_devoir) / len(notes_devoir)

#             return response.Response(
#                 {
#                     'coefficient': coefficient_value, 
#                     'interrogations':notes_interrogation, 
#                     'devoirs': notes_devoir, 
#                     'moyenne_interro': moyenne_interro, 
#                     'moyenne_devoir': moyenne_devoir
#                 }, status=status.HTTP_200_OK)
#         except Eleve.DoesNotExist:
#             return response.Response({'error': 'Eleve not found'}, status=status.HTTP_404_NOT_FOUND)
        

# class CreateorUpdateNoteView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             nouvelles_notes = data.get('nouvellesNotes', [])

#             for note in nouvelles_notes:
#                 try:
#                     note_data =  Note.objects.filter(
#                         matiere_id=int(note['matiere']),
#                         devoir_id=int(note['devoir']),
#                         trimestre_id=int(note['trimestre']),
#                         eleve_id=int(note['eleve']),
#                     )
#                     if note_data:
#                         note_data.update(valeur=int(note['valeur']))
#                     else:
#                         note_data = Note.objects.create(
#                             matiere_id=int(note['matiere']),
#                             devoir_id=int(note['devoir']),
#                             trimestre_id=int(note['trimestre']),
#                             eleve_id=int(note['eleve']),
#                             valeur=int(note['valeur'])
#                         )
            
#                 except exceptions.ValidationError as e:
#                     # La note existe déjà, donc nous l'ignorons
#                     print(e)

#             return response.Response({'message': 'Notes ajoutées avec succès'}, status=status.HTTP_200_OK)
#         except json.JSONDecodeError:
#             return response.Response({'message': 'Erreur de décodage JSON'}, status=status.HTTP_400_BAD_REQUEST)
