from django import forms

import django_filters
from django_filters import FilterSet

from .models import Application, Layer


class ApplicationFilter(FilterSet):
    layer = django_filters.ModelMultipleChoiceFilter(
        queryset=Layer.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Application
        fields = ("layer",)
