from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def recipe(request):
    if request.method=="POST":
        data = request.POST
        # files=request.Files[]
        # print(f"recipe name is {data['name']}")
        # reciptImage=request.FILES.get['iamge']
        reciptImage=request.FILES.get('iamge')

        recipe_name=data['name']
        recipe_description=data.get('ingredient')
        # print(f"recipe name is {data.get('name')}")
        print(f"reciept name is {recipe_name}\n and the description is {recipe_description} \n image of reciept is:{reciptImage}")


    return render(request,"recipe.html",context={"title":"recipe"})