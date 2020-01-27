from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView

from django_filters.views import FilterView

from .filters import ProcessFilter
from .models import Process
from .service import load_zaaktype


class ProcessListView(FilterView):
    model = Process
    template_name = "processes/process_list.html"
    filterset_class = ProcessFilter


class ProcessDetailView(DetailView):
    model = Process
    template_name = "processes/process_detail.html"


class ProcessBpmnView(View):
    def get(self, request, pk):
        process = Process.objects.get(pk=pk)
        return HttpResponse(process.xml(), content_type="text/xml")


class ProcessSOView(ProcessDetailView):
    template_name = "processes/process_so.html"

    def get_context_data(self, **kwargs) -> dict:
        kwargs["zaaktype"] = load_zaaktype(self.object.zaaktype)
        return super().get_context_data(**kwargs)
