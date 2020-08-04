from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Ingredient, Product, ReceipeIngredient


class ProdAdmin(UserAdmin):
	list_display = ("name", "slug", "pk")
	search_fields = ()
	readonly_fields = ()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	ordering = ("pk",)


admin.site.register(Ingredient)
admin.site.register(Product, ProdAdmin)
admin.site.register(ReceipeIngredient)



# class AccountAdmin(UserAdmin):
# 	list_display = ("email", "username", "last_login", "is_staff", "is_active", "calories_plan", "diet_type")
# 	search_fields = ("email", "username", "diet_type",)
# 	readonly_fields = ("date_joined", "last_login")

# 	#Must have properties leave them empty if not need them.
# 	filter_horizontal = ()
# 	list_filter = ()
# 	fieldsets = ()
