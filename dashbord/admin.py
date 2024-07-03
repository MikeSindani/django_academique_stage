from django.contrib import admin
from .models import Faculte, Universite, Entreprise, User, Etudiant, Stage, Cotation

class FaculteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'universite')

class UniversiteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email')

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'status', 'email', 'adresse')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'entreprise', 'universite')

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'promotion', 'faculte', 'filiere', 'Universite')

class StageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'annee', 'date_debut', 'date_fin', 'lieu', 'etudiant', 'universite', 'entreprise')

class CotationAdmin(admin.ModelAdmin):
    list_display = ('regularite', 'connaissance', 'competance', 'dicipline', 'rendement', 'sociabililte', 'etudiant')

admin.site.register(Faculte, FaculteAdmin)
admin.site.register(Universite, UniversiteAdmin)
admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Cotation, CotationAdmin)