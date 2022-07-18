from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nom_categorie


class Produit(models.Model):
    nom_produit = models.CharField(max_length=255)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="produits")
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nom_produit
