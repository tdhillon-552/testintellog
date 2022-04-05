from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic import ListView, View

from .forms import MasterRecordForm, DailyLogAdditionalDetails, BOLOAdditionalFields, PersonsForm
from .models import MasterRecords, AdditionalDetails, Persons
import json


def home(request):
    return render(request, 'home.html')


class CreateBolo(View):

    def get(self, request):
        master_record_data = MasterRecordForm()
        BOLO_additional_data = BOLOAdditionalFields()
        PersonsFormset = formset_factory(PersonsForm)

        content = {
            'master_record_data': master_record_data,
            'BOLO_additional_data': BOLO_additional_data,
            'PersonsFormset': PersonsFormset
        }
        return render(request, 'createbolo.html', content)

    def post(self, request):
        master_record_data = MasterRecordForm(request.POST or None)
        BOLO_additional_data = BOLOAdditionalFields(request.POST or None)
        person_formset = formset_factory(PersonsForm)(request.POST or None)
        if master_record_data.is_valid() and BOLO_additional_data.is_valid() and person_formset.is_valid():
            cleaned_additional_data = {key.strip('x'): value for key, value in
                                       BOLO_additional_data.cleaned_data.items()}

            current_master_record = MasterRecords.objects.create(**master_record_data.cleaned_data,
                                                                 user=request.user,
                                                                 additional_detail=cleaned_additional_data,
                                                                 type_id=2)
            current_master_record.save()

            for person_data in person_formset:
                Persons.objects.create(**person_data.cleaned_data, master_record_id=current_master_record)

        else:
            master_record_data = MasterRecordForm()
            BOLO_additional_data = BOLOAdditionalFields()
            person_formset = formset_factory(PersonsForm)

        content = {
            'master_record_data': master_record_data,
            'BOLO_additional_data': BOLO_additional_data,
            'PersonsFormset': person_formset,

        }

        return render(request, 'createbolo.html', content)


class CreateDailyLog(View):

    def get(self, request):
        master_record_data = MasterRecordForm()
        BOLO_additional_data = DailyLogAdditionalDetails()

        content = {
            'master_record_data': master_record_data,
            'BOLO_additional_data': BOLO_additional_data
        }
        return render(request, 'createdailylog.html', content)

    def post(self, request):
        master_record_data = MasterRecordForm(request.POST or None)
        daily_log_additional_data = DailyLogAdditionalDetails(request.POST or None)
        if master_record_data.is_valid() and daily_log_additional_data.is_valid():
            cleaned_additional_data = {key.strip('x'): value for key, value in
                                       daily_log_additional_data.cleaned_data.items()}

            MasterRecords.objects.create(**master_record_data.cleaned_data,
                                         user=request.user,
                                         additional_detail=cleaned_additional_data,
                                         type_id=2)

        else:
            master_record_data = MasterRecordForm()
            daily_log_additional_data = DailyLogAdditionalDetails()

        content = {
            'master_record_data': master_record_data,
            'daily_log_additional_data': daily_log_additional_data
        }

        return render(request, 'createdailylog.html', content)


class ListMasterRecords(ListView):
    """Home page. Lists pending records"""
    model = MasterRecords
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_details'] = AdditionalDetails.objects.filter(is_active=True).filter(form__type='BOLO')
        return context
