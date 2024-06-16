from django.db import models
import datetime
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser

CLASSROOMS = (
    ('2nde', 'Seconde'),
    ('1ere', 'Premiere'),
    ('Tle', 'Terminale'),
)

EXAMS = (
    ('1ere Interrogation', '1ere Interrogation'),
    ('2eme Interrogation', '2eme Interrogation'),
    ('3eme Interrogation', '3eme Interrogation'),
    ('1er Devoir', '1er Devoir'),
    ('2eme Devoir', '2eme Devoir'),
)

TERMS = (
    ('1er Trimestre', '1er Trimestre'),
    ('2eme Trimestre', '2eme Trimestre'),
    ('3eme Trimestre', '3eme Trimestre'),

)

SEX = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme'),
    ('Autre', 'Autre'),
)

# Create your models here.


class Promotion(models.Model):
    YEAR_CHOICES = [(year, str(year)) for year in range(2020, 2050)]
    current_year = datetime.datetime.now().year

    year_start = models.IntegerField(
        _('Year start'), choices=YEAR_CHOICES, default=current_year)
    year_end = models.IntegerField(
        _('Year end'), choices=YEAR_CHOICES, default=current_year)

    def __str__(self):
        return '{}-{}'.format(self.year_start, self.year_end)

    class Meta:
        db_table = 'promotions'
        managed = True
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'
        unique_together = ('year_start', 'year_end')


class Course(models.Model):
    code = models.CharField(_("Code"), max_length=4, unique=True)

    def __str__(self):
        return f"{self.code}"

    class Meta:
        db_table = 'courses'
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Subject(models.Model):
    code = models.CharField(_("Code "), max_length=9, unique=True)
    name = models.CharField(_("Nom"), max_length=50, unique=True)
    appreciation = models.CharField(
        _("Appreciation"), max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'subjects'
        managed = True
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Classroom(models.Model):

    code = models.CharField(_("Code de la classe"),
                            max_length=9, choices=CLASSROOMS)
    name = models.CharField(_("Nom de la classe"), max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'classes'
        managed = True
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'


class Coefficient(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_(
        "Matiere"), on_delete=models.CASCADE)
    value = models.PositiveIntegerField(_("Coefficient"))
    classroom = models.ForeignKey(
        Classroom, verbose_name=_("Classe"), on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}{}-{}'.format(self.subject.name, self.classroom.name, self.value)

    class Meta:
        db_table = 'coefficients'
        unique_together = ('subject', 'classroom')
        managed = True
        verbose_name = 'Coefficient'
        verbose_name_plural = 'Coefficients'


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=7, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Student(models.Model):

    user = models.OneToOneField(
        User, verbose_name=_(""), on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    father_contact = models.CharField(max_length=255, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    mother_contact = models.CharField(max_length=255, blank=True, null=True)
    tutor_name = models.CharField(max_length=255, blank=True, null=True)
    tutor_contact = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'students'
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


class Teacher(models.Model):

    user = models.OneToOneField(
        User, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        db_table = 'teachers'
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'registries'
        unique_together = ('user', 'promotion')
        managed = True
        verbose_name = 'Registry'
        verbose_name_plural = 'Registries'


class Instruct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    promotion = models.ForeignKey(
        Promotion, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'instructs'
        unique_together = ('promotion', 'classroom', 'subject')
        managed = True
        verbose_name = 'Instruct'
        verbose_name_plural = 'Instructs'


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.CharField(choices=EXAMS, max_length=20)
    term = models.CharField(choices=TERMS, max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.DecimalField(decimal_places=2, max_digits=4)

    class Meta:
        db_table = 'scores'
        unique_together = ('user', 'exam', 'term', 'subject')
        managed = True
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
