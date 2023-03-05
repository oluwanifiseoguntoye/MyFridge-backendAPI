from django.db import models

# Create your models here.
class UserIngredient(models.Model):
    ingredient = models.CharField(max_length=255)

class Recipe(models.Model):
    recipe = models.CharField(max_length=255)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(UserIngredient, on_delete=models.CASCADE)

