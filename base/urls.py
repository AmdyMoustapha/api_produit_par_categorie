from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='accueil'),
    path('ajouter/', views.ajouter_produits, name='ajouter-produits'),
    path('tout_produits/', views.view_produits, name='view_produits'),
    path('DetailProduit/<int:pk>/', views.DetailProduit, name="DetailProduit"),
    path('ajouterC/', views.ajouter_categories, name='ajouter_categories'),
    path('tout_categories/', views.view_categories, name='view_categories'),
    path('produits_par_categorie/<int:pk>/',
         views.produits_par_categorie, name="produits_par_categorie"),
]
