from django.urls import path
from .views import ProfilesListView, registration_view, login_view, logout_view

app_name = "profile"

urlpatterns = [
	path("profile_table/", ProfilesListView.as_view(), name="prof_table"),	
	path("registration/", registration_view, name="registration"),
	path("log_in/", login_view, name="log_in"),
	path("log_out/", logout_view, name="log_out"),

]