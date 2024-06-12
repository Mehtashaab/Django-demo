from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.CharField(max_length=200)
    recipe_image=models.ImageField(upload_to='recipe_image',blank=True)
    recipe_price=models.DecimalField(max_digits=9,decimal_places=2)