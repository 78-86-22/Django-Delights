from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"