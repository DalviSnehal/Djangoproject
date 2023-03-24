from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name='about'),
    path('introduction', views.introduction, name='introduction'),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('myimagepage', views.myimagepage, name='myimagepage'),
    path('myimagepage2', views.myimagepage2, name='myimagepage2'),
    path("displayimages", views.displayimages, name="displayimages"),

]
