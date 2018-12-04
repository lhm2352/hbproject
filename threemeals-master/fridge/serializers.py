from fridge.models import Ingredient
from rest_framework import serializers

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ingredient
		fields = ('ingredientName', 'type', 'category', 'storageMethod', 'unit', 'defaultValue', 'ingredientCode')

"""
ingredientName= models.CharField(max_length=50)
    type=models.IntegerField(default=0)
    category=models.IntegerField(default=0)
    storageMethod=models.IntegerField(default=0)
    unit=models.CharField(max_length=100)
    defaultValue=models.IntegerField(default=0)
    ingredientCode=models.IntegerField(default=0)
"""