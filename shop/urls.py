from django.urls import path
from . import views


urlpatterns = [
		path('',views.accueil_view,name='accueil'),
		path('panier/',views.panier_view,name='panier'),
		path('confirmation/',views.confirmation_view,name='confirmation'),
		path('show/<int:id>/',views.detail_view,name='show'),
	
 ]