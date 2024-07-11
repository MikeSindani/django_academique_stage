from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Universite(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    
class Faculte (models.Model):
    nom = models.CharField(max_length=200,unique=True)
    email = models.EmailField(default="exemple@gmail.com")
    def __str__(self, *args, **kwds) :
        return "{}".format(self.nom)

class Entreprise (models.Model):
    nom = models.CharField(max_length=200,unique=True)
    status = models.CharField(max_length=200)
    email = models.EmailField()
    adresse = models.CharField(max_length=200)

class User(AbstractUser): # encadeur univeersiteur et entreprise utilisateur du systeme 
  # Pas besoin de définir le champ username
  username = models.CharField(max_length=200, unique=True)
  email = models.EmailField('email address', unique=True)
  entreprise = models.ForeignKey("Entreprise", on_delete=models.SET_NULL, null=True, blank=True)
  faculte = models.ForeignKey("Faculte", on_delete=models.SET_NULL, null=True, blank=True)
  
  isEntreprise= models.BooleanField(default=False)
  isFaculte = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['password','username'] 
  def __str__(self):
      return "{} - {}".format(self.username,self.email)


# Create your models here.
class Etudiant(models.Model):
     matricule = models.CharField(max_length=200,primary_key=True)
     nom = models.CharField(max_length=200) 
     prenom = models.CharField(max_length=200)  
     promotion = models.CharField(max_length=200)
     faculte =  models.ForeignKey("Faculte", on_delete=models.SET_NULL,null=True)
     filiere = models.CharField(max_length=200)
     entreprise = models.ForeignKey("Entreprise", on_delete=models.SET_NULL,null=True)
     faculte = models.ForeignKey("Faculte", on_delete=models.SET_NULL, null=True, blank=True)
     email = models.EmailField(null=True, blank=True)
     phone = models.CharField(max_length=200, null=True, blank=True)

     def __str__(self):
       return "{}".format(self.nom)
     
class Stage (models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    annee = models.CharField(max_length=200)
    date_inscription = models.DateField(null=True)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    lieu = models.CharField(max_length=200,null=True,blank=True)
    etudiant = models.ForeignKey("Etudiant", on_delete=models.SET_NULL,null=True)
    faculte = models.ForeignKey("Faculte", on_delete=models.SET_NULL, null=True, blank=True)
    entreprise = models.ForeignKey("Entreprise", on_delete=models.SET_NULL,null=True)
    encadeur = models.ForeignKey("User", on_delete=models.SET_NULL,null=True)
    isStage = models.BooleanField(default=False)
    
class Cotation  (models.Model):
    regularite = models.IntegerField()
    connaissance = models.IntegerField()
    competance = models.IntegerField()
    dicipline = models.IntegerField()
    rendement = models.IntegerField()
    sociabililte = models.IntegerField()
    etudiant = models.ForeignKey("Etudiant",on_delete=models.SET_NULL,null=True) 