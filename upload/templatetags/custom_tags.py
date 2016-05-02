from django import template

register = template.Library()

@register.filter(name='format')
def format(value):
	res = value
	if len(value) > 0 and value[len(value) - 1] != "\"":
		res = value[1:-3]
	elif len(value) > 0:
		res = value[1:-1]
	return res



