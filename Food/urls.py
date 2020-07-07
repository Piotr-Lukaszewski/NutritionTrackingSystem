from django.urls import path
from .views import ProductsTableView, ingredient_creation_choice

app_name = "food"

urlpatterns = [
    path("prod_table/", ProductsTableView.as_view(), name="prod_table"),
    path("ingredient_creation_form/", ingredient_creation_choice, name="ingredient_choice" )
]
