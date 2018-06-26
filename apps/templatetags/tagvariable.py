from django import template

register = template.Library()

@register.simple_tag
def flag():
    return True

@register.simple_tag
def nosoy():
    return 'nosoy'

