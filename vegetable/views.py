from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
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
        # complete_data=f"u have entered the {recipe_name} as name and as  "
        # complete_data=
        # print(f"recipe name is {data.get('name')}")
        print(f"reciept name is {recipe_name}\n and the description is {recipe_description} \n image of reciept is:{reciptImage}")
        
        Recipe.objects.create(
            name=recipe_name,
            ingredient=recipe_description,
            review=reveiw_star,
            iamge=reciptImage,
        )
        # in our case automatically it is redirect but for safety put this 
        return redirect("/recipe/")
    # return render(request,"Intableformat.html",context={"title":"recipe","dbdata":Recipe.objects.all()[0].name+Recipe.objects.all()[1].name})
    AllQuery=Recipe.objects.all()
    # code for searching
    if request.GET.get("search"):
        AllQuery=AllQuery.filter(name__icontains = request.GET.get("search"))
        # return AllQuery
        # print(request.GET.get("search"))



    # return render(request,"recipe.html",context={"title":"recipe","dbdata":Recipe.objects.all()})
    return render(request,"recipe.html",context={"title":"recipe","dbdata":AllQuery})

    # return render(request,"Intableformat.html",context={"title":"recipe","dbdata":Recipe.objects.all()})
def delete_recipe(request,id):
    querytodelete=Recipe.objects.get(id=id)
    querytodelete.delete()
    return redirect("/recipe/")
    # print(id)
    # return HttpResponse("sleep")
def update_recipe(request,id):
    ValaueToUpdate=Recipe.objects.get(id=id)
    # updateData=request.POST
    if request.POST:
        updateData=request.POST
        ValaueToUpdate.name=updateData.get('name')
        ValaueToUpdate.ingredient=updateData.get('ingredient')
        ValaueToUpdate.review=updateData.get("review")
        if request.FILES.get('iamge'):
            ValaueToUpdate.iamge=request.FILES.get("iamge")    
                #TO take image from user to store it in datavase we have to use word which has the request inside that files will be there and then from that files import files then using the get import the name  
        ValaueToUpdate.save()
        return redirect("/recipe/")
        
    # return HttpResponse(id)
    return render(request,"update.html",context={"value":ValaueToUpdate,"DATA":updateData})
    # Recipe.objects.get(id=id).update(name="kishore")