from django.urls import path
from .views import (
                    #Product
					ProductsTableView, 
					SearchResultsView, 					
                    ProductUpdateView,
                    ProductDetailView,
                    ProductDeleteView,
                    #Recipe
					create_product,
					add_ingredient,
					create_recipe,
                    #Ingredient
                    CreateIngredient, 
                    IngredientDetailView,
                    IngredientTableView,
                    IngredientUpdateView,
                    ProductDeleteView,

)

app_name = "food"

urlpatterns = [
    #Product part
    path("prod_table/", ProductsTableView.as_view(), name="prod_table"),
    path("prod_detail/<int:pk>/", ProductDetailView.as_view(), name="prod_detail"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path("prod_update/<int:pk>/",ProductUpdateView.as_view(), name="update_prod"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_prod"),
    #Meal & recipe part
    path("meal_create/", create_product, name="meal_create"),
    path("ingredients_table/<int:pk>/", add_ingredient, name="ingredient_table"),
    path("add_ingredient_to_recipe/<int:prod_pk>/<int:ing_pk>/", create_recipe, name="create_recipe"),
    #Ingredients part
    path("ingredient_table/", IngredientTableView.as_view(), name="ingredinet_table"),
    path("ingredient_add/", CreateIngredient.as_view(), name="ingredinet_create"),
    path("ingredient_detail/<int:pk>/", IngredientDetailView.as_view(), name="ingredinet_detail"),
    path("ingredient_update/<int:pk>/",IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredient_delete/<int:pk>/",ProductDeleteView.as_view(), name="ingredient_delete"),

]
