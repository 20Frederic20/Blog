from django.db import models
from django.utils.translation import gettext as _


TYPES_DEVOIRS =(
    ('INTERRO', 'INTERROGATION'),
    ('DEVOIR', 'DEVOIR'),
)

import datetime

# Create your models here.
class Classe(models.Model):
    code = models.CharField(_("Code de la classe"), max_length=9, unique=True)
    libelle = models.CharField(_("Nom de la classe"), max_length=50, unique=True)

    def __str__(self):
        return f"{self.code}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'


class Promotion(models.Model):
    YEAR_CHOICES = [(year, str(year)) for year in range(1900, 2101)]
    current_year = datetime.datetime.now().year

    anneeDebut = models.IntegerField(_('Year start'), choices=YEAR_CHOICES, default=current_year)
    anneeFin = models.IntegerField(_('Year end'), choices=YEAR_CHOICES, default=current_year)

    def __str__(self):
        return '{}-{}'.format(self.anneeDebut, self.anneeFin)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
        unique_together=('anneeDebut', 'anneeFin')


class Filiere(models.Model):
    codeFiliere = models.CharField(_("Code"), max_length=4, unique=True)
    nomFiliere = models.CharField(_("Nom "), max_length=50, unique=True)

    def __str__(self):
        return f"{self.nomFiliere}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Filiere'
        verbose_name_plural = 'Filieres'


class Trimestre(models.Model):
    codeTrimestre = models.PositiveIntegerField(_("Trimestre "), unique=True)

    def __str__(self):
        return f"{self.codeTrimestre}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Trimestre'
        verbose_name_plural = 'Trimestres'

class Devoir(models.Model):
    code = models.PositiveIntegerField(_("Devoir "))
    type = models.CharField(max_length=7, choices=TYPES_DEVOIRS, default="INTERRO")
    denomination = models.CharField(_("Denomination"), max_length=50, null=True)

    def __str__(self):
        return f"{self.denomination}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devoir'
        verbose_name_plural = 'Devoirs'


class Matiere(models.Model):
    codeMatiere = models.CharField(_("Code "), max_length=9, unique=True)
    denomination = models.CharField(_("Nom"), max_length=50)
    appreciation = models.CharField(_("Appreciation"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.denomination}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'
    
class Coefficient(models.Model):
    matiere = models.ForeignKey("classes.Matiere", verbose_name=_("Matiere"), on_delete=models.CASCADE, null=True)
    valeur = models.PositiveIntegerField(_("Coefficient"))
    classe = models.ForeignKey("classes.Classe", verbose_name=_("Classe"), on_delete=models.CASCADE, null=True)
    filiere = models.ForeignKey("classes.Filiere", verbose_name=_("Filiere"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}-{}{}-{}'.format(self.matiere, self.classe.codeClasse, self.filiere.codeFiliere, self.valeur)

    class Meta:
        db_table = ''
        unique_together=('matiere', 'filiere', 'classe')
        managed = True
        verbose_name = 'Coefficient'
        verbose_name_plural = 'Coefficients'