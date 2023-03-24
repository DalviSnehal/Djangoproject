from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello")


def about(request):
    return HttpResponse("This is the about page")


def introduction(request):
    return HttpResponse("This is the Django introduction")


def myfirstpage(request):
    return render(request, 'index.html')





def myimagepage(request):
    return render(request, 'imagefile.html')

def myimagepage2(request):
    return render(request, 'imagefile2.html')

def displayimages(request):
    return render(request, 'exerciseday22_Q1.html')