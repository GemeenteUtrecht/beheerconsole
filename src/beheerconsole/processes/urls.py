from django.urls import path

from .views import ProcessDetailView, ProcessListView

app_name = 'processes'

urlpatterns = [
    path('', ProcessListView.as_view(), name='process-list'),
    path("<pk>/", ProcessDetailView.as_view(), name="process-detail"),
]
