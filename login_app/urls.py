from django.urls import path
from .views import *

urlpatterns = [
    path('', login,name="connexion"),
    path('post_login',post_logIn,name="post_login"),
]