from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class Eleve(models.Model):

    user = models.ForeignKey("users.User", verbose_name=_(""), on_delete=models.CASCADE)
    filiere = models.ForeignKey("classes.Filiere", verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    classe = models.ForeignKey("classes.Classe", verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    promotion = models.ForeignKey("classes.Promotion", verbose_name=_(""), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Eleve")
        verbose_name_plural = _("Eleves")

    def __str__(self):
        return f"{self.user.username}"
    

class Note(models.Model):
    matiere = models.ForeignKey("classes.Matiere", verbose_name=_("Matiere"), on_delete=models.SET_NULL, null=True)
    devoir = models.ForeignKey("classes.Devoir", verbose_name=_("Devoir "), on_delete=models.SET_NULL, null=True)
    trimestre = models.ForeignKey("classes.Trimestre", verbose_name=_("Trimestre"), on_delete=models.SET_NULL, null=True)
    eleve = models.ForeignKey("Eleve", verbose_name=_("Eleve"), on_delete=models.CASCADE)
    valeur = models.PositiveIntegerField(_("Note"))
    def __str__(self):
        return '{}-{}'.format(self.matiere, self.valeur)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        unique_together = ('matiere', 'devoir', 'trimestre', 'eleve')

