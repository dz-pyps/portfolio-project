from django import template

register = template.Library()


def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter(name='ck')
def ck(value):
    """ Return a Unicode string of one character """
    return chr(value)


