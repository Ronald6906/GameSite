from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('cart', views.cart,name="cart"),
    path('eldenring', views.eldenring,name="eldenring"),
    path('forzahorizon', views.forzahorizon,name="forzahorizon"),
    path('gtav', views.gtav,name="gtav"),
    path('re4', views.re4,name="re4"),
    path('spiderman', views.spiderman,name="spiderman"),
    path('uncharted', views.uncharted,name="uncharted"),
    path('warhammer', views.warhammer,name="warhammer"),
    path('witcher', views.witcher,name="witcher"),
    path('index', views.index,name="index"),
    path('register/', views.register , name="register")

]