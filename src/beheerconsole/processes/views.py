from django.views.generic import DetailView

from django_filters.views import FilterView

from .filters import ProcessFilter
from .models import Process


class ProcessListView(FilterView):
    model = Process
    template_name = "processes/process_list.html"
    filterset_class = ProcessFilter


class ProcessDetailView(DetailView):
    model = Process
    template_name = "processes/process_detail.html"
