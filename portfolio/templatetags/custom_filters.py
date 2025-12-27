from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """Split a string by the given separator"""
    return value.split(arg)

@register.filter(name='trim')
def trim(value):
    """Remove leading and trailing whitespace"""
    return value.strip()
