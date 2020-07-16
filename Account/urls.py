from django.urls import path


from Account.views import (
	ProfilesListView,
	profile_update_view, 
	registration_view, 
	login_view, 
	logout_view, 
	profile_view
	)

app_name = "profile"

urlpatterns = [
	path("profile_table/", ProfilesListView.as_view(), name="prof_table"),	
	path("registration/", registration_view, name="registration"),
	path("log_in/", login_view, name="log_in"),
	path("log_out/", logout_view, name="log_out"),
	path("details/", profile_view, name="profile_details"),
	path("update/", profile_update_view, name="profile_update"),
]







