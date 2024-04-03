from typing import Any
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import IngredientForm, MenuForm, RecipeForm
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class HomeView(TemplateView):
    template_name = "inventory/home.html"

class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"
    
class AddIngredientView(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
        
class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm
    
class MenuListView(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItem.objects.all()
        return context
   
class AddMenu_itemView(CreateView):
    model = MenuItem
    template_name = "inventory/add_dish.html"
    form_class = MenuForm

class RecipesListView(TemplateView):
    model = RecipeRequirement
    template_name = "inventory/recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItem.objects.all()
        return context
    
class AddRecipeView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe.html"
    form_class = RecipeForm

