from django.contrib import admin
from django.contrib import admin
from .models import User, Eleve, Note
from classes.models import Devoir, Classe, Matiere, Promotion, Coefficient

admin.site.register(User)
admin.site.register(Eleve)
admin.site.register(Devoir)
admin.site.register(Note)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Coefficient)
admin.site.register(Promotion)