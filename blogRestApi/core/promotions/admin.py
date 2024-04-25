from django.contrib import admin
from .models import User, Student, Teacher, Promotion, Classroom, Course, Coefficient, Subject, Register, Instruct, Score
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Promotion)
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Coefficient)
admin.site.register(Register)
admin.site.register(Instruct)
admin.site.register(Score)