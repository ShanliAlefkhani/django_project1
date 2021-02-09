from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
	context = {
		"articles": [
			{
				"title": "Earth",
				"description": "This is the Earth",
				"img": "https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/maps-satellite-images/satellite-image-of-globe.jpg"
			}
		]
	}
	return render(request, "blog/home.html", context)
