from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produit
from .models import Categorie
from .serializers import ProduitSerializer
from .serializers import CategorieSerializer

from rest_framework import serializers
from rest_framework import status
# Create your views here.

# ---------------------menu-----------------------


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'tout_les_produits': 'http://127.0.0.1:8000/tout_produits',
        'Detail_des_Produit': 'http://127.0.0.1:8000/DetailProduit/pk',
        'toutes_les_categories': 'http://127.0.0.1:8000/tout_categories',
        'Ajouter_un_produit': 'http://127.0.0.1:8000/ajouter',
        'Ajouter_une_categorie': 'http://127.0.0.1:8000/ajouterC',
        'produits_par_categorie': 'http://127.0.0.1:8000/produits_par_categorie/pk',
    }

    return Response(api_urls)

# ---------------------ajouter produit-----------------------


@api_view(['POST'])
def ajouter_produits(request):
    produit = ProduitSerializer(data=request.data)

    # validating for already existing data
    if Produit.objects.filter(**request.data).exists():
        raise serializers.ValidationError('cette donne existe déjà')

    if produit.is_valid():
        produit.save()
        return Response(produit.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ---------------------Liste produits-----------------------


@api_view(['GET'])
def view_produits(request):

    # checking for the parameters from the URL
    if request.query_params:
        produits = Produit.objects.filter(**request.query_param.dict())
    else:
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)

    # if there is something in items else raise error
    if produits:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ---------------------détail produits-----------------------


@api_view(['GET'])
def DetailProduit(request, pk):
    if request.method == 'GET':
        produits = Produit.objects.get(id=pk)
        print(produits)
        serializer = ProduitSerializer(produits, many=False)
    return Response(serializer.data)

# ---------------------ajouter categorie-----------------------


@api_view(['POST'])
def ajouter_categories(request):
    categorie = CategorieSerializer(data=request.data)

    # validating for already existing data
    if Categorie.objects.filter(**request.data).exists():
        raise serializers.ValidationError('cette donne existe déjà')

    if categorie.is_valid():
        categorie.save()
        return Response(categorie.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ---------------------Liste categories-----------------------


@api_view(['GET'])
def view_categories(request):

    # checking for the parameters from the URL
    if request.query_params:
        categories = Categorie.objects.filter(**request.query_param.dict())
    else:
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)

    # if there is something in items else raise error
    if categories:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# ---------------------Liste produits par categorie-----------------------

@api_view(['GET'])
def produits_par_categorie(request, pk):
    if request.method == 'GET':
        produits = Produit.objects.filter(categorie=pk)
        print(produits)
        serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)
