from django.urls import path
from .views import (
					ProductsTableView, 
					SearchResultsView, 
					CreateIngredient, 
                    ProductUpdateView,
                    ProductDetailView,
                    ProductDeleteView,
					create_product,
					add_ingredient,
					create_recipe,

)

app_name = "food"

urlpatterns = [
    #Product part
    path("prod_table/", ProductsTableView.as_view(), name="prod_table"),
    path("prod_detail/<int:pk>", ProductDetailView.as_view(), name="prod_detail"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path("prod_update/<int:pk>",ProductUpdateView.as_view(), name="update_prod"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="delete_prod"),
    #Ingredients part
    path("ingredient_add/", CreateIngredient.as_view(), name="ingredinet_create"),
    #Meal & recipe part
    path("meal_create/", create_product, name="meal_create"),
    path("ingredients_table/<int:pk>", add_ingredient, name="ingredient_table"),
    path("add_ingredient_to_recipe/<int:prod_pk>/<int:ing_pk>", create_recipe, name="create_recipe")

]
