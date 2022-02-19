from django.urls import path
from .views import TabNameList, TableListView


app_name = 'summary_per_hour'


urlpatterns = [
    path('', TabNameList.as_view(), name='index'),
    path('<date_selected>/<tab_name>/', TableListView.as_view()),
# url(r'^(?P<user_id>\d+)', views.Man, name='man'),
]