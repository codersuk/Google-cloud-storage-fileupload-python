from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(req):
    return JsonResponse({'status': 'ok', 'Support': 'b@icelabz.co.uk'})
