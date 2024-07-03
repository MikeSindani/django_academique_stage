from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Faculte (models.Model):
    nom = models.CharField(max_length=200)
    universite = models.CharField(max_length=200)
class Universite(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()

class Entreprise (models.Model):
    nom = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    email = models.EmailField()
    adresse = models.CharField(max_length=200)

class User(AbstractUser): # encadeur univeersiteur et entreprise utilisateur du systeme 
  # Pas besoin de définir le champ username
  username = models.CharField(max_length=200, unique=True)
  email = models.EmailField('email address', unique=True)
  entreprise = models.ForeignKey("Entreprise", on_delete=models.SET_NULL, null=True, blank=True)
  universite = models.ForeignKey("Universite", on_delete=models.SET_NULL, null=True, blank=True)

  isEntreprise= models.BooleanField(default=False)
  isUnversite = models.BooleanField(default=False)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['password'] 
  def __str__(self):
      return "{} - {}".format(self.username,self.email)


# Create your models here.
class Etudiant(models.Model):
     matricule = models.CharField(max_length=200,primary_key=True)
     nom = models.CharField(max_length=200) 
     prenom = models.CharField(max_length=200)  
     promotion = models.CharField(max_length=200)
     faculte = models.CharField(max_length=200)
     filiere = models.CharField(max_length=200)
     Universite = models.ForeignKey("Universite", on_delete=models.SET_NULL,null=True)

     def __str__(self):
       return "{}".format(self.nom)
     
class Stage (models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    annee = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=200)
    etudiant = models.ForeignKey("Etudiant", on_delete=models.SET_NULL,null=True)
    universite = models.ForeignKey("Universite", on_delete=models.SET_NULL,null=True)
    entreprise = models.ForeignKey("Entreprise", on_delete=models.SET_NULL,null=True)
    
class Cotation  (models.Model):
    regularite = models.IntegerField()
    connaissance = models.IntegerField()
    competance = models.IntegerField()
    dicipline = models.IntegerField()
    rendement = models.IntegerField()
    sociabililte = models.IntegerField()
    etudiant = models.ForeignKey("Etudiant",on_delete=models.SET_NULL,null=True)