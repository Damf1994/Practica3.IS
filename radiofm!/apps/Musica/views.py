from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


def index(request):
    return HttpResponse("<h1> Bienvenidos a TuradioFM!!! </h1>")


def top_songs(request):
	
	return HttpResponse(
		"<head><title>Canciones populares</title></head>"
        "<body><h1>Estas son las canciones populares:</h1></body>"
        )



class IndexView(TemplateView):
	
	template_name = 'Musica/index.html'
	


class Top_SongsView(TemplateView):
	
	template_name = 'Musica/top_songs.html'
	
