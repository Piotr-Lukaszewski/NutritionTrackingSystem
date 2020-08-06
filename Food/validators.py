from django.core.exceptions import ValidationError


def macro_quantity_validator(value):
	if value > 100:
		raise ValidationError(
			(f"Page quantity ({value}) cannot be lower than 0."),
			params={"value": value},
		)



		