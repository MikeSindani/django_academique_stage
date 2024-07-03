from django.shortcuts import render,redirect
from .models import Etudiant, Universite, Entreprise,Faculte, Stage, Cotation,User
from django.http import JsonResponse


# Create your views here.
def dashboard(request):
    totals__entreprise = Entreprise.objects.all().count()
    totals__universite = Universite.objects.all().count()
    entreprises = Entreprise.objects.all()
    return render(
        request,
        "dashboard/dashboard.html",
        {
            "totals__universite": totals__universite,
            "totals__entreprise": totals__entreprise,
            "entreprises": entreprises,
        },
    )

def ajouter_entreprise (request):
    return render(request, "dashboard/ajouter_entreprise.html")

def ajouter_etudiant (request):
    entreprises = Entreprise.objects.all()
    universites = Universite.objects.all()
    return render(request, "dashboard/ajouter_etudiant.html", {"entreprises": entreprises, "universites": universites})


def create_entreprise(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        status = request.POST['status']
        email = request.POST['email']
        adresse = request.POST['adresse']
        entreprise = Entreprise(nom=nom, status=status, email=email, adresse=adresse)
        entreprise.save()
        message = 'Entreprise créée avec succès !'
        return render(request, 'dashboard/ajouter_entreprise.html', {'message': message})
    return render(request, 'dashboard/ajouter_entreprise.html')


def create_etudiant(request):
    if request.method == 'POST':
        matricule = request.POST['matricule']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        promotion = request.POST['promotion']
        faculte_id = request.POST['faculte']
        filiere = request.POST['filiere']
        universite_id = request.POST['universite']
        universite = Universite.objects.get(id=universite_id)
        faculte = Faculte.objects.get(id=faculte_id)
        entreprise_id = request.POST['entreprise']
        entreprise = Entreprise.objects.get(id=entreprise_id)
        etudiant = Etudiant(matricule=matricule, nom=nom, prenom=prenom, promotion=promotion, faculte=faculte, filiere=filiere, Universite=universite,entreprise=entreprise)
        etudiant.save()
        etudiants = Etudiant.objects.all()
        message = 'Étudiant créé avec succès !'
        return render(request, 'dashboard/ajouter_etudiant.html', {'message': message})
    universites = Universite.objects.all()
    return render(request, 'dashboard/ajouter_etudiant.html', {'universites': universites,"etudiants":etudiants})

# views.py



def api_faculties(request):
    q = request.GET.get('q', '')
    faculties = Faculte.objects.filter(universite=q)
    data = [{'id': faculty.id, 'nom': faculty.nom} for faculty in faculties]
    return JsonResponse(data, safe=False)


def liste_stagaires(request):
    entreprise_id = request.user.entreprise
    print(entreprise_id)
    etudiants = Etudiant.objects.filter(entreprise=entreprise_id)
    return render(request, 'dashboard/liste_stagaire.html', {"etudiants": etudiants})

# views.py
from django.shortcuts import render, redirect
from .models import Stage, Etudiant, Universite, Entreprise

def stage(request):
    stages = Stage.objects.all()
    return render(request, 'dashboard/stage.html', {
        'stages': stages,
    })

def commenece_stage(request, etudiant_id):
    etudiant = Etudiant.objects.get(matricule=etudiant_id)
    return render(request, 'dashboard/create_stage.html',{"etudiant": etudiant})


# views.py


def create_stage(request, etudiant_id):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        annee = request.POST.get('annee')
        date_debut = request.POST.get('date_debut')
        etudiant = Etudiant.objects.get(matricule=etudiant_id)
        universite_id = etudiant.Universite.id
        universite = Universite.objects.get(id=universite_id)
        entreprise_id = request.user.entreprise.id
        entreprise = Entreprise.objects.get(id=entreprise_id)
        encadreur_id = request.user.id
        encadreur = User.objects.get(id=encadreur_id)


        project = Stage(
            titre=titre,
            description=description,
            annee=annee,
            date_debut=date_debut,
            etudiant=etudiant,
            universite=universite,
            entreprise=entreprise,
            encadeur=encadreur
        )
        project.save()
        stages = Stage.objects.all()
        return render(request, 'dashboard/stage.html', {
            'stages': stages, "message": 'Stage peut étre commence avec succes !'
        })
    else:
        return render(request, 'dashboard/stage.html')