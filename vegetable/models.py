from django.db import models
# for authentication  
from  django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    ingredient=models.TextField()
    review=models.CharField(max_length=10)
    iamge=models.ImageField(upload_to="recipe",null=True)
# this is automatically called integerfield  
    recipe_counter=models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.name 

