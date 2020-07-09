from django.urls import path
from .views import ProductsTableView, SearchResultsView

app_name = "food"

urlpatterns = [
    path("prod_table/", ProductsTableView.as_view(), name="prod_table"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
