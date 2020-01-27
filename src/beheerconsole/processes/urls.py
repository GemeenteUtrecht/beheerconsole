from django.urls import path

from .views import ProcessBpmnView, ProcessDetailView, ProcessListView, ProcessSOView

app_name = "processes"

urlpatterns = [
    path("", ProcessListView.as_view(), name="process-list"),
    path("<pk>/", ProcessDetailView.as_view(), name="process-detail"),
    path("<pk>/bpmn", ProcessBpmnView.as_view(), name="process-bpmn"),
    path("<pk>/so/", ProcessSOView.as_view(), name="process-so"),
]
