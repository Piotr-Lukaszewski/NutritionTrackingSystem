from django.urls import path
from .views import ProfilesListView

app_name = "profile"

urlpatterns = [
    path("profile_table/", ProfilesListView.as_view(), name="prof_table"),

]