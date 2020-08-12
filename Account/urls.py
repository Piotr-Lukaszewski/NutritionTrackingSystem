from django.urls import path


from Account.views import (
	ProfilesListView,
	profile_update_view, 
	registration_view, 
	login_view, 
	logout_view, 
	profile_view,
	add_prod_to_diet,
	DietView,
	DeleteDietProdView,
	UpdateDietProdView,
	)

app_name = "profile"

urlpatterns = [
	path("profile_table/", ProfilesListView.as_view(), name="prof_table"),	
	path("registration/", registration_view, name="registration"),
	path("log_in/", login_view, name="log_in"),
	path("log_out/", logout_view, name="log_out"),
	path("details/", profile_view, name="profile_details"),
	path("update/", profile_update_view, name="profile_update"),
	path("add_to_diet/<int:pk>", add_prod_to_diet, name="add_to_diet"),
	path("user_diet/<str:username>/", DietView.as_view(), name="user_diet"),
	path("user_diet/remove/<int:pk>/", DeleteDietProdView.as_view(), name="remove_position"),
	path("user_diet/update/<int:pk>/", UpdateDietProdView.as_view(), name="update_position_weight"),
]







