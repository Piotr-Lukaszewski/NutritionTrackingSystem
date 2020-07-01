from django.contrib import admin
from .models import Ingredient, Product, ReceipeIngredient


admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(ReceipeIngredient)


