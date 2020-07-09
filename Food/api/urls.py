from django.urls import path

from .views import IngredientListAPI, IngredientDetailsAPI

app_name = "food_api"

urlpatterns = [
    path("", IngredientListAPI.as_view(), name='api_ingredient_view'),
    path("<int:pk>/", IngredientDetailsAPI.as_view(), name="api_ingredient_detail_view")
    # path("food_search/", get_list_by_name, name="ingredinet_search")
]
