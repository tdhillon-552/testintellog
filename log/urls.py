from django.urls import path
from . import views
from .views import ListMasterRecords

urlpatterns = [
    path('', views.home, name='home'),
    path('entry/dailylog', views.CreateDailyLog.as_view(), name='createdailylog'),
    path('entry/bolo', views.CreateBolo.as_view(), name='createbolo'),

    path('search/dailylog', ListMasterRecords.as_view(), name='listmasterrecords')
]
