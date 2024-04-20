from typing import Any
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from .forms import IngredientForm, MenuForm, RecipeForm
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"


# below: views that let the user see current inventory, 
# add new ingredients, update stock and delete ingredients

class IngredientView(LoginRequiredMixin, ListView):
    model = Ingredient 
    template_name = "inventory/ingredients.html"
    
class AddIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm
        
class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = reverse_lazy("ingredients")


 #  below: views for the user to see the menu, add new dishes, 
 #  add their recipes, see all the recipes and delete dishes from menu
   
class MenuListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class AddMenu_itemView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_dish.html"
    form_class = MenuForm

class AddRecipeView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/add_recipe.html"
    form_class = RecipeForm

class RecipesListView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MenuItem.objects.all()
        return context
    
class DeleteMenu_itemView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/delete_dish.html"
    success_url = reverse_lazy("menu")


# view that decreases ingredient quantities in stock and registers purchases made
    
class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/add_purchase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = [dishes for dishes in MenuItem.objects.all() if dishes.available()]
        return context
    
    def post(self, request):
        dish = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=dish)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item = menu_item)

        for item in requirements.all():
            stock_ingredient = item.ingredient
            stock_ingredient.quantity -= item.quantity
            stock_ingredient.save()
        
        purchase.save()
        return redirect("/Menu")
    
    
# below: views for user to see reports of purchases made and revenue
   
class ReportsView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

class PuchasesReportView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases_report.html"
    
class RevenueReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/revenue_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sales"] = Purchase.objects.all()
        revenue = 0
        cost = 0
        for item in Purchase.objects.all():
            revenue += item.menu_item.price
            for requirement in item.menu_item.reciperequirement_set.all():
                cost += requirement.ingredient.unit_price * requirement.quantity
        
        context["revenue"] = revenue
        context["cost"] = cost
        context["profit"] = revenue - cost
        return context

def user_logout(request):
    logout(request)
    return redirect("/")