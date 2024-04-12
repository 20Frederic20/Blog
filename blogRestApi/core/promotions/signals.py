from django.db.models.signals import post_save, post_init, pre_save
from django.dispatch import receiver
from .models import User, Teacher, Student
from django.contrib.auth.hashers import make_password
from django.conf import settings
from rest_framework.authtoken.models import Token
import json
    
@receiver(post_save, sender=User)
def create_teacher_or_student(sender, instance, created, **kwargs):
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
# def encrypt_password(sender, instance, **kwargs):
#     if instance._state.adding or 'last_name' in instance.__dict__:
#         original_instance = sender.objects.filter(pk=instance.pk).first()
#         # if not original_instance or original_instance.password != instance.password:
#         if not original_instance:
#             instance.username = str(instance.last_name.lower() + str(sender.objects.count()))
#             instance.password = make_password(instance.username)
def encrypt_password(sender, instance, **kwargs):
    if instance._state.adding:
        if not instance.email:
            instance.email = instance.username + '@example.com'
        password = User.objects.make_random_password()
        instance.username = password
        instance.password = make_password(password)