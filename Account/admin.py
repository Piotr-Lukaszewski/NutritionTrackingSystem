from django.contrib import admin
from Account.models import Profile, Diet, User_Diet
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
	list_display = ("email", "username", "last_login", "is_staff", "is_active", "calories_plan", "diet_type")
	search_fields = ("email", "username", "diet_type",)
	readonly_fields = ("date_joined", "last_login")

	#Must have properties leave them empty if not need them.
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class ProductsAdmin(UserAdmin):
	list_display = ("date", "profile", "product", "weight")
	search_fields = ()
	readonly_fields = ()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ("date",)


admin.site.register(Profile, AccountAdmin)
admin.site.register(Diet, ProductsAdmin)
admin.site.register(User_Diet)


