from rest_framework import serializers
from .models import (Classroom, Coefficient, Course, Instruct, Promotion, Register, Score, Student,
                     Subject, Teacher, User)
from django.contrib.auth.hashers import make_password

CLASSROOMS = (
    ('2nde', 'Seconde'),
    ('1ere', 'Premiere'),
    ('Tle', 'Terminale'),
)


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ['id', 'year_start', 'year_end']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'code']


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'code', 'name', 'appreciation']


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ['id', 'code', 'name', 'course']
        extra_kwargs = {'name': {"required": False}}

    # def perform_create(self, serializer):
    #     # Get the course instance based on the provided code
    #     course = Course.objects.get(code=serializer.validated_data['course'])

    #     # Iterate through CLASSROOMS to find the corresponding name
    #     for value in CLASSROOMS:
    #         if value[0] == serializer.validated_data['code']:
    #             name = value[1] + course.code
    #             # Set the 'name' field of the instance
    #             serializer.validated_data['name'] = name

    #     # Call serializer.save() to create the instance
    #     # serializer.save()


class CoefficientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coefficient
        fields = ['id', 'subject', 'classroom', 'value']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_student',
                  'is_teacher', 'is_administrator', 'is_director', 'sex', 'age']
        extra_kwargs = {'username': {'required': False}, 'email': {
            'required': False}, 'password': {'required': False}}


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'user', 'father_name', 'mother_name', 'tutor_name']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = {
            'id': instance.user.id,
            'username': instance.user.username,
            'email': instance.user.email,
        }
        representation['user'] = user_representation
        return representation


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ['id', 'user', 'classroom', 'promotion']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = {
            'id': instance.user.id,
            'username': instance.user.username,
            'email': instance.user.email,
        }
        representation['user'] = user_representation
        classroom_representation = {
            'id': instance.classroom.id,
            'code': instance.classroom.code,
            'name': instance.classroom.name,
        }
        representation['classroom'] = classroom_representation
        promotion_representation = {
            'id': instance.promotion.id,
            'year_start': instance.promotion.year_start,
            'year_end': instance.promotion.year_end,
        }
        representation['promotion'] = promotion_representation
        return representation


class InstructSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instruct
        fields = ['id', 'user', 'classroom', 'promotion', 'subject']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = {
            'id': instance.user.id,
            'username': instance.user.username,
            'email': instance.user.email,
        }
        representation['user'] = user_representation
        classroom_representation = {
            'id': instance.classroom.id,
            'code': instance.classroom.code,
            'name': instance.classroom.name,
        }
        representation['classroom'] = classroom_representation
        promotion_representation = {
            'id': instance.promotion.id,
            'year_start': instance.promotion.year_start,
            'year_end': instance.promotion.year_end,
        }
        representation['promotion'] = promotion_representation
        subject_representation = {
            'id': instance.subject.id,
            'code': instance.subject.code,
            'name': instance.subject.name,
            'appreciation': instance.subject.appreciation,
        }
        representation['subject'] = subject_representation
        return representation


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ['id', 'user', 'exam', 'term', 'subject', 'value']
