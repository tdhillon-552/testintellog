from django import template

from log.models import AdditionalDetails

register = template.Library()


def label(value, arg):
    if arg == "bolo":
        labels_from_db = AdditionalDetails.objects.filter(is_active=True).filter(form__type='BOLO').values('id', 'display_name')
        for labels in labels_from_db:
            if str(labels['id']) == value:
                value = labels['display_name']
        print(value)
    return value


register.filter('label', label)
