from django.core.exceptions import ValidationError


def macro_quantity_validator(value):
	if value > 100:
		raise ValidationError(
			(f"{value} > 100 You can't type more than 100g of macroingredients per 100g of product."),
			params={"value": value},
		)
	elif value < 0:
		raise ValidationError(
			(f"{value} < 0 You can't type less than 0g of macroingredients per 100g of product."),
			params={"value": value},
		)

def price_validator(value):
	if value > 200:
		raise ValidationError(
			(f"Price {value}$ is incorrect, you cannot enter a price higher than 199.99$"),
			params={"value": value},
		)
		
def weight_validaotr(value):
	if value > 500:
		raise ValidationError(
			(f"You cannot enter weight ({value}), the suggested portion must not exceed 500 grams"),
			params={"value": value},
		)
	elif value < 0:
		raise ValidationError(
				(f"You can't type suggested portion less than 0."),
				params={"value": value},
			)