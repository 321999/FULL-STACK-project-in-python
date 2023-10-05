from django.shortcuts import render
from django.http import HttpRequest
from .models import *
# Create your views here.
def recipe(request):
    if request.method=="POST":
        data = request.POST
        # files=request.Files[]
        # print(f"recipe name is {data['name']}")
        # reciptImage=request.FILES.get['iamge']
        reciptImage=request.FILES.get('iamge')

        recipe_name=data['name']
        # we are fetching data like this becaus we know that data is in object form 
        recipe_description=data.get('ingredient')
        reveiw_star=data.get('review')
        # print(f"recipe name is {data.get('name')}")
        print(f"reciept name is {recipe_name}\n and the description is {recipe_description} \n image of reciept is:{reciptImage}")
        Recipe.objects.create(
            name=recipe_name,
            ingredient=recipe_description,
            review=reveiw_star,
            iamge=reciptImage,
        )

    return render(request,"recipe.html",context={"title":"recipe"})