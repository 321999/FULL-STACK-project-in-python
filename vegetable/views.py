from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def recipe(request):
    data = request.POST
    print(data)
    return render(request,"recipe.html",context={"title":"recipe"})