from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .views import IngredientListAPI, IngredientDetailsAPI

schema_view = get_swagger_view(title="My Swagger")

app_name = "food_api"

urlpatterns = [
    path("", IngredientListAPI.as_view(), name='api_ingredient_view'),
    path("<int:pk>/", IngredientDetailsAPI.as_view(), name="api_ingredient_detail_view"),
    path("swagger/", schema_view)
    # path("food_search/", get_list_by_name, name="ingredinet_search")
]
