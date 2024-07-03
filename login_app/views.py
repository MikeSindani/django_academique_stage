from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .decorations import unauthentificated_user
from django.contrib.auth import logout
from dashbord.models import *
from django.http import HttpResponseRedirect
# Create your views here.
def login(request):
    return render(request, 'login/login.html')


@unauthentificated_user
def post_logIn(request):
    if request.method == "POST" : 
        
        email = request.POST.get("email")
        password  = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
                login(request,user)
                
                return redirect("dashbord")
        else:   
                 # Créer un objet HttpResponse avec les données à envoyer
                response = HttpResponseRedirect("connexion")
                # Retourner la réponse
                return response
                
    else:
           return render(request, 'login/login.html')