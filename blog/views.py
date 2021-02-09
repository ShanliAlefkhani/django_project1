from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
	return HttpResponse("Hello, World!!")


def api(request):
	data = {
		"1": {
			"title": "maqale aval",
			"id": 20,
			"slug": "first.article"
		},
		"2": {
			"title": "maqale dovom",
			"id": 21,
			"slug": "second.article"
		}
	}
	return JsonResponse(data)
