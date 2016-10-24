#from django.shortcuts import render
# Create your views here.
#views.py creates the different website page views for the specific url

from django.http import HttpResponse

# the name of the url/view page = views.index = index
def index(request):
	return HttpResponse("<h1> Startpage - Übersicht - Einleitung ... </h1>")


