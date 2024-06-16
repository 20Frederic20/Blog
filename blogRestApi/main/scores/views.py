from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, exceptions, response, status
from rest_framework.views import APIView
import json

from main.promotions.models import Score, Subject, User
from main.promotions.serializers import ScoreSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        exam = self.request.GET.get("exam", None)
        term = self.request.GET.get("term", None)
        subject_id = self.request.GET.get("subject_id", None)
        subject = Subject.objects.filter(pk=subject_id).first()

        queryset = Score.objects.all()

        if term:
            queryset = queryset.filter(term=term)

        if exam:
            queryset = queryset.filter(exam=exam)

        if subject:
            queryset = queryset.filter(subject=subject)

        return queryset


class CreateorUpdateScoreView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            scores = json.loads(request.body.decode("utf-8"))
            print(scores)
            for score in scores:
                try:
                    user = User.objects.filter(pk=score["user"]).first()
                    subject = Subject.objects.filter(pk=score["subject"]).first()
                    Score.objects.update_or_create(
                        user=user,
                        exam=score["exam"],
                        subject=subject,
                        term=score["term"],
                        defaults={"value": float(score["value"])},
                    )

                except exceptions.ValidationError as e:
                    # La note existe déjà, donc nous l'ignorons
                    print(e)

            return response.Response(
                {"message": "Notes ajoutées avec succès"}, status=status.HTTP_200_OK
            )
        except json.JSONDecodeError:
            return response.Response(
                {"message": "Erreur de décodage JSON"},
                status=status.HTTP_400_BAD_REQUEST,
            )


# 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
