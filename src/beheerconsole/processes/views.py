from django.views.generic import DetailView, ListView

from .models import Process


class ProcessListView(ListView):
    model = Process
    template_name = "processes/process_list.html"


class ProcessDetailView(DetailView):
    model = Process
    template_name = "processes/process_detail.html"
