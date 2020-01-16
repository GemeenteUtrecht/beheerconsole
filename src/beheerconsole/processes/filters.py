from django import forms

import django_filters
from django_filters import FilterSet

from .models import Department, Process


class ProcessFilter(FilterSet):
    department = django_filters.ModelMultipleChoiceFilter(
        queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Process
        fields = ("department",)
