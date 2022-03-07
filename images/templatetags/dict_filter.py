from django import template


register=template.Library()

@register.filter(name='dict_value')

def dict_value(value,arg):
  print(arg)
  print(value)
  return value.get(arg)