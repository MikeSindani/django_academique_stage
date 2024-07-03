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
def logIn(request):
    return render(request, 'login/login.html')



def post_login(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request=request, user=user)
                print(user)
                return redirect('dashbord')  # Correction de la faute de frappe
            else:
                return render(request, 'login/login.html', {'msg': 'Invalid email or password'})
        except Exception as e:
            # Gestion des exceptions
            print(f"Error during authentication: {e}")
            return render(request, 'login/login.html', {'msg': 'An error occurred.'})
    else:
        return render(request, 'login/login.html')