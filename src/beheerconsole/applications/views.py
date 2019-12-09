from django.views.generic import DetailView, ListView

from .models import Application


class ApplicationListView(ListView):
    model = Application
    template_name = "applications/application_list.html"


class ApplicationDetailView(DetailView):
    model = Application
    template_name = "applications/application_detail.html"
