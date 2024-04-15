from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("Ingredients/", views.IngredientView.as_view(), name="ingredients"),
    path("Reports/", views.ReportsView.as_view(), name="reports"),   
    path("Menu/", views.MenuListView.as_view(), name="menu"),
    path("Menu/add_menu_item",views.AddMenu_itemView.as_view(), name="add_dish"),
    path("Menu/Recipes", views.RecipesListView.as_view(), name="recipes"),
    path("Recipes/add_recipe", views.AddRecipeView.as_view(), name="requirements"),
    path("Ingredients/add_ingredient", views.AddIngredientView.as_view(), name="add_ingredient"),
    path("ingredients/<slug:pk>/update_ingredient", views.UpdateIngredientView.as_view(), name="update_ingredient"),
    path("Purchases", views.PuchasesReportView.as_view(), name="purchases"),
    path("Menu/Purchases", views.NewPurchaseView.as_view(), name="add_purchase"),
    path("Revenue", views.RevenueReportView.as_view(), name="revenue"),
    path("logout/", views.user_logout, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    ]
