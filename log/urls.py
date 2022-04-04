from django.urls import path
from . import views
from .views import ListMasterRecords

urlpatterns = [
    path('', views.home, name='home'),
    path('entry/dailylog', views.daily_log_view, name='dailylogview'),
    path('search/dailylog', ListMasterRecords.as_view(), name='listmasterrecords')
]
