from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorations import unauthentificated_user
from django.contrib.auth import logout
from dashbord.models import *
from django.http import HttpResponseRedirect


# Create your views here.
def logIn(request):
    return render(request, "login/login.html")


def signup(request):
    entreprise = Entreprise.objects.all()
    faculte = Faculte.objects.all()
    return render(request, "login/signup.html", {"entreprises": entreprise , "facultes":faculte})


def post_login(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request=request, user=user)
                print(user)
                return redirect("dashbord")  # Correction de la faute de frappe
            else:
                return render(
                    request, "login/login.html", {"msg": "Invalid email or password"}
                )
        except Exception as e:
            # Gestion des exceptions
            print(f"Error during authentication: {e}")
            return render(request, "login/login.html", {"msg": "An error occurred."})
    else:
        return render(request, "login/login.html")


def create_account(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        status = request.POST["status"]
        isEntreprise_req = request.POST.get("isEntreprise", False)
        entreprise_id = request.POST.get("entreprise")
        isUnversite_req = request.POST.get("isUnversite", False)
        isEntreprise = False
        isUniversite = False
        if isEntreprise_req == "entreprise":
            isEntreprise = True
            isFaculte = False
            entreprise = Entreprise.objects.get(id=entreprise_id)
        elif isUnversite_req == "universite":
            isEntreprise = False
            isFaculte = True
            faculte = Faculte(nom=username,email=email)
            faculte.save()
        else:
            isEntreprise = False
            isFaculte = False
        

        user = User(username=username, email=email)
        user.set_password(password)
        if isEntreprise_req == "entreprise":
            user.entreprise = entreprise
        else : 
           faculte = Faculte.objects.get(nom=username)
           user.faculte = faculte
        user.isEntreprise = isEntreprise
        user.isFaculte = isFaculte
        try:
            user.save()
            user_log = authenticate(username=email, password=password)
            login(request, user_log)
            return redirect("dashbord")
        except Exception as e:
            entreprise = Entreprise.objects.all()
            faculte = Faculte.objects.all()
            return render(
                request, "login/signup.html", {"msg": str(e), "entreprises": entreprise , 'facultes':  faculte}
            )
    entreprise = Entreprise.objects.all()
    faculte = Faculte.objects.all()
    return render(request, "login/signup.html", {"msg": "", "entreprises": entreprise , 'facultes':  faculte})
