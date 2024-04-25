from django.db.models.signals import post_save, post_init, pre_save
from django.dispatch import receiver
from .models import User, Teacher, Student, Classroom, Course
from django.contrib.auth.hashers import make_password
from django.conf import settings
from rest_framework.authtoken.models import Token
import json

CLASSROOMS =(
    ('2nde', 'Seconde'),
    ('1ere', 'Premiere'),
    ('Tle', 'Terminale'),
)
    
@receiver(post_save, sender=User)
def after_saving_user(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teacher.objects.create(user=instance)
        elif instance.is_student:
            Student.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(pre_save, sender=User)
def before_saving_user(sender, instance, **kwargs):
    if instance._state.adding:
        if not instance.email:
            instance.email = instance.username + '@example.com'
        password = User.objects.make_random_password()
        instance.username = password
        instance.password = make_password(password)

@receiver(pre_save, sender=Classroom)
def before_saving_course(sender, instance, **kwargs):
    if instance._state.adding:
        if instance.code and instance.course:
            course = Course.objects.get(code=instance.course)
            for value in CLASSROOMS:
                if value[0] == instance.code:
                    instance.name = value[1] + ' ' + course.code