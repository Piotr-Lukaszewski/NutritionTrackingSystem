from django.urls import path
from .views import ProductsTableView

app_name = "food"

urlpatterns = [
    path("prod_table/", ProductsTableView.as_view(), name="prod_table"),
]
