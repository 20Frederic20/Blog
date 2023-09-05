from django.db import models
from django.utils.translation import gettext as _


TYPES_DEVOIRS =(
    ('INTERRO', 'INTERROGATION'),
    ('DEVOIR', 'DEVOIR'),
)

class YearField(models.PositiveIntegerField):
    description = "A field to store a year."

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [self.validate_year]
        super(YearField, self).__init__(*args, **kwargs)

    def validate_year(self, value):
        if value < 1000 or value > 9999:
            raise models.ValidationError("Enter a valid year (between 1000 and 9999).")

# Create your models here.
class Classe(models.Model):
    codeClasse = models.CharField(_("Code de la classe"), max_length=9, unique=True)
    libelleClasse = models.CharField(_("Nom de la classe"), max_length=50, unique=True)

    def __str__(self):
        return f"{self.codeClasse}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'


class Promotion(models.Model):
    anneeDebut = YearField(unique=True)
    anneeFin = YearField(unique=True)

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
    codeDevoir = models.PositiveIntegerField(_("Devoir "))
    typeDevoir = models.CharField(max_length=7, choices=TYPES_DEVOIRS, default="INTERRO")
    denominationDevoir = models.CharField(_("Denomination"), max_length=50, null=True)

    def __str__(self):
        return f"{self.denominationDevoir}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Devoir'
        verbose_name_plural = 'Devoirs'


class Matiere(models.Model):
    codeMatiere = models.CharField(_("Code "), max_length=7)
    denomination = models.CharField(_("Nom"), max_length=50)
    classeMatiere = models.ManyToManyField("classes.Classe", verbose_name=_("Classe"), related_name='matieres_autorisees')
    filiereMatiere = models.ManyToManyField("classes.Filiere", verbose_name=_("Filiere"), related_name='filieres_autorisees')
    appreciation = models.CharField(_("Appreciation"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.denomination}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Matiere'
        verbose_name_plural = 'Matieres'
    
class Coefficient(models.Model):
    matiereCoefficient = models.ForeignKey("classes.Matiere", verbose_name=_("Matiere"), on_delete=models.CASCADE, null=True)
    valeurCoefficient = models.PositiveIntegerField(_("Coefficient"))

    def __str__(self):
        return '{}-{}'.format(self.matiereCoefficient, self.valeurCoefficient)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Coefficient'
        verbose_name_plural = 'Coefficients'


class Note(models.Model):
    matiereNote = models.ForeignKey("classes.Matiere", verbose_name=_("Matiere"), on_delete=models.SET_NULL, null=True)
    devoirNote = models.ForeignKey("classes.Devoir", verbose_name=_("Devoir "), on_delete=models.SET_NULL, null=True)
    trimestreDevoir = models.ForeignKey("classes.Trimestre", verbose_name=_("Trimestre"), on_delete=models.SET_NULL, null=True)
    eleve = models.ForeignKey("users.Eleve", verbose_name=_("Eleve"), on_delete=models.CASCADE)
    valeurNote = models.PositiveIntegerField(_("Note"))
    def __str__(self):
        return '{}-{}'.format(self.matiereNote, self.valeurNote)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        unique_together = ('matiereNote', 'devoirNote', 'trimestreDevoir', 'eleve')