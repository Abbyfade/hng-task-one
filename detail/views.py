from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    responseData = {
        "slackUsername": "abby10", 
        "backend": True, 
        "age": 21,
        "bio": "Hi there! I'm Abiola, a medical student and a tech enthusiast, i'm in the backend track of hng9"
    }
    return JsonResponse(responseData, headers=header)