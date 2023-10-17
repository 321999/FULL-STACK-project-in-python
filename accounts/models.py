import uuid
from django.db import models

# Create your models here.
class yv(models.model):
    video=models.FileField(upload_to="utube")

# thsi class  should be accessible to everyone 
class Base(models.Model):
    uid=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    # uuid is the unique which is generated 
    created_AT=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True
        # the model is not created for this 
        # so that it automatically all the field is accesible to the class who is going to call it 
class Color(Base):
    # all teh filed of base is automatically called and creatd inside the color table
    color_code=models.CharField(max_length=50)


class people(Base):
    # name,about,age,email(unique),
    name=models.CharField(max_length=20)
    about=models.TextField()
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    # didnot understand this 
    color=models.ManyToManyField(Color)

class PA(Base):
    people=models.ForeignKey(people,on_delete=models.SET_NULL)
    # related name is for reverse relationship 
    address=models.TextField() 