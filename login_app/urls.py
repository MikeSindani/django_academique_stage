from django.urls import path
from .views import *

urlpatterns = [
    path('', logIn,name="connexion"),
    path('post_login',post_login,name="post_login"),
    path('signup',signup,name="signup"),
    path('create_account/', create_account, name='create_account'),
]