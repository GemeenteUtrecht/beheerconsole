from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from django_filters.views import FilterView

from .filters import ApplicationFilter
from .models import Application


class ApplicationListView(LoginRequiredMixin, FilterView):
    model = Application
    template_name = "applications/application_list.html"
    filterset_class = ApplicationFilter


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = "applications/application_detail.html"
