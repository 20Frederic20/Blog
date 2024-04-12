from rest_framework import serializers
from .models import (Classroom, Coefficient, Course, Instruct, Promotion, Register, Score, Student,
    Subject, Teacher, User)
from django.contrib.auth.hashers import make_password


class PromotionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Promotion
        fields = ['id', 'year_start', 'year_end']
        

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'code', 'name']
        

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ['id', 'code', 'name', 'appreciation']
        

class ClassroomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classroom
        fields = ['id', 'code', 'name', 'course']
        

class CoefficientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coefficient
        fields = ['id', 'subject', 'classroom', 'value']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_student', 'is_teacher', 'is_administrator', 'is_director', 'sex', 'age']
        extra_kwargs = {'username': {'required': False}, 'email': {'required': False}, 'password': {'required': False}}
        
        
        

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'user', 'father_name', 'mother_name', 'tutor_name']
        
        
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ['id', 'user']
        

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Register
        fields = ['id', 'user', 'classroom', 'promotion']
        

class InstructSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Instruct
        fields = ['id', 'user', 'classroom', 'promotion', 'subject']
        

class ScoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Score
        fields = ['id', 'user', 'exam', 'term', 'subject', 'value']