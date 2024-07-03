from django.urls import path
from .views import *

urlpatterns = [
    path('', logIn,name="connexion"),
    path('post_login',post_login,name="post_login"),
]