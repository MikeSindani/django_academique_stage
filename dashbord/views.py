from django.shortcuts import render
from .models import Etudiant, Universite, Entreprise

# Create your views here.
def dashboard (request):
    totals__entreprise = Entreprise.objects.all().count()
    totals__universite = Universite.objects.all().count()
    return render(request, 'dashboard/dashboard.html',{'totals__universite':totals__universite,'totals__entreprise':totals__entreprise})