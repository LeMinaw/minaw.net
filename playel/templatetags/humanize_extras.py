#-*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter
def altapnumber(value):
    """An alternate version of the apnumber filter, using a different string list.
    It's handy in  handling name genres in particular languages (such as French, "une").
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    if not 0 < value < 10:
        return value
    return ('une', 'deux', 'trois', 'quatre', 'cinq',
            'six', 'sept', 'huit', 'neuf')[value - 1]


@register.filter(safe=False)
def altpluralize(value, arg='s'):
    """
    An alternate version of the pluralize filter. The only difference is that if the 
    value is zero, it returns the singular suffix. It is handy in handling the
    "Zero case" in certain languages (such as French, "aucun vote").
    """
    if ',' not in arg:
        arg = ',' + arg
    bits = arg.split(',')
    if len(bits) > 2:
        return ''
    singular_suffix, plural_suffix = bits[:2]

    try:
        if float(value) > 1:
            return plural_suffix
    except ValueError:  # Invalid string that's not a number.
        pass
    except TypeError:  # Value isn't a string or a number; maybe it's a list?
        try:
            if len(value) > 1:
                return plural_suffix
        except TypeError:  # len() of unsized object.
            pass
    return singular_suffix
