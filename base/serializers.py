from django.db.models import fields
from rest_framework import serializers
from .models import Produit
from .models import Categorie


class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = ('id', 'nom_categorie',)


class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = ('id', 'nom_produit', 'categorie', 'description')
