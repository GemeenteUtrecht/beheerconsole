from django.views.generic import DetailView, ListView

from django_filters.views import FilterView

from .filters import ApplicationFilter
from .models import Application


class ApplicationListView(FilterView):
    model = Application
    template_name = "applications/application_list.html"
    filterset_class = ApplicationFilter


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "applications/application_detail.html"
