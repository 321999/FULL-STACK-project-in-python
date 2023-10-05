from django.db import models

# Create your models here.

class Recipe(models.Model):
    name=models.CharField(max_length=50)
    ingredient=models.TextField()
    review=models.CharField(max_length=10)
    iamge=models.ImageField(upload_to="recipe",null=True)

    def __str__(self) -> str:
        return self.name 