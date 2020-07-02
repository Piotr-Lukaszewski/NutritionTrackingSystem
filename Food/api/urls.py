from django.urls import path

from .views import IngredientList

urlpatterns = [
    path('', IngredientList.as_view(), name='api_ingredient_view'),
]
