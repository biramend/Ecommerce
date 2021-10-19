from django.db import models

# Create your models here.
class Categorie(models.Model):
	name = models.CharField(max_length=200)
	date_ajout = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_ajout']

	def __str__(self):
		return self.name 

class Produit(models.Model):
	titre = models.CharField(max_length=200)
	price = models.FloatField()
	description = models.TextField()
	categorie = models.ForeignKey(Categorie,related_name='categorie',on_delete=models.CASCADE)
	image = models.CharField(max_length=500)
	date_ajout = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_ajout']
		
	def __str__(self):
		return self.titre

class Commande(models.Model):
	items = models.CharField(max_length=300)
	total = models.CharField(max_length=300)
	nom = models.CharField(max_length=150)
	phone =models.CharField(max_length=250,unique=True) 
	email = models.EmailField()
	password = models.CharField(max_length=150,default="pass123")
	adresse = models.CharField(max_length=150)
	ville = models.CharField(max_length=150)
	pays = models.CharField(max_length=150)
	zipcode = models.CharField(max_length=150)
	date_commade = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering =['-date_commade']

	def __str__(self):
		return self.nom