from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home_view"),
    #NEW APPLICATION URLS
    path("food/", include("Food.urls")),
    path("profile/", include("Account.urls")),
    #REST FRAMEWORK URLS
    path("api/", include("Food.api.urls")),
]
