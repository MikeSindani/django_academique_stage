from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashbord"),
    path('ajouter_entreprise/', ajouter_entreprise, name='ajouter_entreprise'),
    path('ajouter_etudiant/', ajouter_etudiant, name='ajouter_etudiant'),
    path('create_entreprise/', create_entreprise, name='create_entreprise'),
    path('create_etudiant/', create_etudiant, name='create_etudiant'),
    path('api/faculties/', api_faculties, name='api_faculties'),
    path('logout/', logOut, name='logout'),
    path('stage/', stage, name='stage'),
    path('liste_stagaires/', liste_stagaires, name='liste_stagaires'),
    path("commence_stage/<str:etudiant_id>/",commenece_stage,name="commence_stage"),
    path("create_stage/<str:etudiant_id>/",create_stage,name="create_stage"),
    path('fin_du_stage/<str:etudiant_id>/', fin_stage, name='fin_stage'),
    path('terminer_stage/<str:etudiant_id>/', terminer_stage, name='terminer_stage'),
    
]
