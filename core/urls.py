
"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))     
"""      

from django.contrib import admin 
from django.urls import path
from core import settings  
from home.views import *  
from vegetable.views import * 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static

urlpatterns = [
    path("register/",register,name="register"),
    path("login/",loginPage,name="login"),
    path("delete-recipe/<id>/",delete_recipe,name="delete_recipe"),
    path("update-recipe/<id>/",update_recipe,name="update-recipe"),
    path("recipe/",recipe,name="recipe"),
    path("contact/",contact,name="contact"),
    path("about/",about,name="about"),
    path("index/",samaan,name="samaan"),
    path("sucess/",sucess,name="sucess"),
    path("ki/raam/h",helo,name="helo"),
    path("blog/",blog,name="blog"),
    path("",helo,name="helo"),
    path('admin/', admin.site.urls),
    path("product/",samaan,name="samaan"),
    path("logout/",logoutuser,name="logout")
]

   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns +=staticfiles_urlpatterns()
# init file is used to delete the file 
# admin file is used to modify the model 
# models.py is used to interact with t eh database 
# to check the fuctionality in the we use test.py 
# views.py all the logical part is writtian inside this 
# in any website login register page is called the functionality to pack this functinality in some module called app 
# project ke module ko divide krte hin us cheez ko app kehte hin  

# to send the data form the backend we use context and in frontedn we use {{name_of_context}}