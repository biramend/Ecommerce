from django.contrib import admin

# Register your models here.
from .models import Categorie , Produit,Commande
 
 

class AdminCategorie(admin.ModelAdmin):
	list_display = ('name', 'date_ajout')
    

class AdminProduit(admin.ModelAdmin):
	search_fields = ('titre',)
	list_display = ('titre','price','categorie','date_ajout')
	# list_editable = ('price',)

    # search_fields = ('titre')
class AdminCommande(admin.ModelAdmin):
	list_display = ('items','total','nom','email','phone','adresse','ville','pays','date_commade')

admin.site.site_header = "SandiaraShop"
admin.site.site_title = "Shoping"
admin.site.index_title = "DG SandiaraShop"

admin.site.register(Produit,AdminProduit)
admin.site.register(Categorie,AdminCategorie)
admin.site.register(Commande,AdminCommande)