from django.shortcuts import render
from django.views.generic import ListView

from .forms import MasterRecordForm, DailyLogAdditionalDetails, BOLOAdditionalFields
from .models import MasterRecords, AdditionalDetails
import json


def home(request):
    return render(request, 'home.html')


def daily_log_view(request):
    if request.method == 'POST':
        master_record_data = MasterRecordForm(request.POST or None)
        BOLO_additional_data = BOLOAdditionalFields(request.POST or None)
        if master_record_data.is_valid() and BOLO_additional_data.is_valid():

            cleaned_additional_data = {key.strip('x'): value for key, value in BOLO_additional_data.cleaned_data.items()}
            print(cleaned_additional_data)
            MasterRecords.objects.create(**master_record_data.cleaned_data,
                                         user=request.user,
                                         additional_detail=cleaned_additional_data)

    else:
        master_record_data = MasterRecordForm()
        BOLO_additional_data = BOLOAdditionalFields()

    content = {
        'master_record_data': master_record_data,
        'BOLO_additional_data': BOLO_additional_data
    }

    return render(request, 'dailylogentry.html', content)


class ListMasterRecords(ListView):
    """Home page. Lists pending records"""
    model = MasterRecords
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_details'] = AdditionalDetails.objects.filter(is_active=True).filter(form__type='BOLO')
        return context
