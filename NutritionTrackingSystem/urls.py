from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home_view"),
    #NEW APPLICATION URLS
    path("food/", include("Food.urls")),
    path("profile/", include("Account.urls")),
    #REST FRAMEWORK URLS
    path("api/", include("Food.api.urls")),
    #Email built-in aps
	path(
		"password_reset/", 
		views.PasswordResetView.as_view(template_name="Account/password_reset.html"), 
		name="password_reset"
	),
	path(
		"password_reset/done/", 
		views.PasswordResetDoneView.as_view(template_name="Account/password_reset_done.html"), 
		name="password_reset_done"
	),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(
             template_name='Account/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
	path(
		"password_reset/changed/done/", 
		views.PasswordResetCompleteView.as_view(template_name="Account/password_reset_complete.html"), 
		name="password_reset_complete"
	),
]
