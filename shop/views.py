from django.shortcuts import redirect, render
from .models import Categorie
from .models import Produit
from .models import Commande

# Create your views here.
def accueil_view(request):
	produits = Produit.objects.all()
	categories = Categorie.objects.all()
	produit_item = request.GET.get('items-produit')
	if produit_item !=' ' and produit_item is not None:
		produits = Produit.objects.filter(titre__icontains=produit_item)

	context = {'produits':produits,'categories':categories}
	return render(request,'shop/index.html',context)


def detail_view(request,id):
	produit = Produit.objects.get(id=id)
	context = {'produit':produit}
	return render(request,'shop/show.html',context)


def panier_view(request):
	if request.method == "POST":
		items = request.POST.get('items')
		total = request.POST.get('total')
		nom = request.POST.get('nom')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		password = request.POST.get('password')
		adresse = request.POST.get('adresse')
		ville = request.POST.get('ville')
		pays = request.POST.get('pays')
		zipcode = request.POST.get('zipcode')
		com =Commande(items=items,total=total,nom=nom,phone=phone,email=email,password=password,adresse=adresse,ville=ville,pays=pays,zipcode=zipcode)
		com.save()
		return redirect('confirmation')
	return render(request,'shop/panier.html')


def confirmation_view(request):
	info = Commande.objects.all()[:1]
	for item in info:
		nom = item.nom
		adresse = item.adresse

	return render(request,'shop/confirmation.html',{'nom':nom,'adresse':adresse})