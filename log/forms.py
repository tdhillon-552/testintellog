
from django import forms
from .models import AdditionalDetails, PersonTypes


class MasterRecordForm(forms.Form):
    violation = forms.CharField(max_length=10, label='Violation')
    date = forms.DateField(label='Date')
    time = forms.TimeField(label='Time')
    title = forms.CharField(max_length=50)
    case_number = forms.CharField(max_length=10)
    cad_call_number = forms.IntegerField()
    cad_id = forms.IntegerField()
    rms_case_number = forms.IntegerField()
    rms_id = forms.IntegerField()


class PersonsForm(forms.Form):
    entity_type  =                 forms.ModelChoiceField(queryset=PersonTypes.objects.filter(is_active=True))
    last_name    =                 forms.CharField(max_length=50)
    first_name   =                 forms.CharField(max_length=50)


class DailyLogAdditionalDetails(forms.Form):
    type_check = AdditionalDetails.objects.filter(is_active=True).filter(form__type='Daily Log')

    for items in type_check:
        if items.type.__str__() == 'checkbox':
            locals()['x' + items.pk.__str__()] = forms.BooleanField(label=items.display_name)
        elif items.type.__str__() == 'text box':
            locals()['x' + items.pk.__str__()] = forms.CharField(label=items.display_name)
        elif items.type.__str__() == 'numerical value':
            locals()['x' + items.pk.__str__()] = forms.IntegerField(label=items.display_name)


class BOLOAdditionalFields(forms.Form):

    type_check = AdditionalDetails.objects.filter(is_active=True).filter(form__type='BOLO')

    for items in type_check:
        if items.type.__str__() == 'checkbox':
            locals()['x'+items.pk.__str__()] = forms.BooleanField(label=items.display_name)
        elif items.type.__str__() == 'text box':
            locals()['x'+items.pk.__str__()] = forms.CharField(label=items.display_name)
        elif items.type.__str__() == 'numerical value':
            locals()['x'+items.pk.__str__()] = forms.IntegerField(label=items.display_name)


