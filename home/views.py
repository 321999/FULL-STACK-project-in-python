from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helo(request):
    return HttpResponse("<h1>welcome to ur home page</h1>")

