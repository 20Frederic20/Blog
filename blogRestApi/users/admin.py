from django.contrib import admin
from django.contrib import admin
from .models import User, Eleve
from classes.models import Devoir, Note, Classe, Matiere, Promotion

admin.site.register(User)
admin.site.register(Eleve)
admin.site.register(Devoir)
admin.site.register(Note)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Promotion)