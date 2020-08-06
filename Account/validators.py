from django.core.exceptions import ValidationError
import datetime


def calories_validator(value):
	if value < 600:
		raise ValidationError(
				(f"Calories plan cannot be smaller than 600 kcals."),
				params={"value": value},
			)
	elif value > 9999:
		raise ValidationError(
				(f"Calories plan cannot be bigger than 9.999 kcals."),
				params={"value": value},
			)

def meal_weight_valdiator(value):
	if meal_weight_valdiator < 0:
		raise ValidationError(
			(f"You cannot choose serving size smaller than 0."),
			params={"value": value},
		)