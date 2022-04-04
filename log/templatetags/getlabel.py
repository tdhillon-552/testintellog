from django import template

from log.models import AdditionalDetails

register = template.Library()


def label(value, arg):
    if arg == "bolo":
        value = AdditionalDetails.objects.filter(form__type='BOLO').filter(id=value).values_list('display_name', flat=True)[0]
    return value


register.filter('label', label)
