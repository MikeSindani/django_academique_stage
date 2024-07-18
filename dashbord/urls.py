from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashbord"),
    # ajouter cree entreprise
    path('ajouter_entreprise/', ajouter_entreprise, name='ajouter_entreprise'),
    path('list_entreprises/', liste_entreprises, name='list_entreprises'),
    path('create_entreprise/', create_entreprise, name='create_entreprise'),
    # ajout des l'etudiants
    path('ajouter_etudiant/', ajouter_etudiant, name='ajouter_etudiant'),
    path('create_etudiant/', create_new_etudiant, name='create_etudiant'),
    path('list_etudiants/', liste_etudiants, name='liste_etudiants'),
    # affectation des l'etudiants
    path('affecter_etudiant/<str:etudiant_id>/', affecter_etudiant, name='affecter_etudiant'),
    path('create_affectation_etudiant/', create_affectation_etudiant, name='create_affectation_etudiant'),
    path('list_etudiant_affecter/', list_etudiant_affecter, name='list_etudiant_affecter'),
    path('list_evaluation', list_evaluation, name='list_evaluation'),
    
    #path("ajouter_faculte", ajouter_faculte, name="ajouter_faculte"),
    #path('list_facultes/', list_facultes, name='list_facultes'),
    path('create_filiere/', create_filiere, name='create_filiere'),
    #path('delete_faculte/<int:pk>/', delete_faculty, name='delete_faculty'),
    
    path('api/faculties/', api_faculties, name='api_faculties'),
    path('logout/', logOut, name='logout'),
    # stages 
    path('list_stagaires/', liste_stagaires, name='liste_stagaires'),
    path('stage/', stage, name='stage'),
    path("commence_stage/<str:etudiant_id>/",commenece_stage,name="commence_stage"),
    path("create_stage/<str:etudiant_id>/",create_stage,name="create_stage"),
    path('fin_du_stage/<str:etudiant_id>/', fin_stage, name='fin_stage'),
    path('terminer_stage/<str:etudiant_id>/', terminer_stage, name='terminer_stage'),

    path('list_cotation/', cotations, name='cotations'),
    path('export_cotations/', export_cotations_to_csv, name='export_cotations_to_csv'),
    path('export_stages/', export_stages_to_csv, name='export_stages_to_csv'),
    
    
]
