from django import template

register = template.Library()


@register.filter(name = 'but')
def cut(value,arg):
    return value.replace(arg, '')


#register.filter('cut',cut)
