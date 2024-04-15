from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0.00)

    def __str__(self):
        return f"name={self.name}; quantity={self.quantity}; unit={self.unit}; unit_price={self.unit_price}"
    
    def get_absolute_url(self):
        return "/Ingredients"

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    
    def __str__(self):
        return f"title={self.title}; price={self.price}"
    
    def available(self):
        return all(dishes.enough() for dishes in self.reciperequirement_set.all())
    
    def get_absolute_url(self):
        return "/Menu"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.00)

    def __str__(self):
        return f"dish={self.menu_item.title}; ingredient={self.ingredient.name}; needs={self.quantity}"
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
    def get_absolute_url(self):
        return "/Menu/Recipes"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"dish={self.menu_item}; time={self.timestamp}"
    
    def get_absolute_url(self):
        return "/Menu"
