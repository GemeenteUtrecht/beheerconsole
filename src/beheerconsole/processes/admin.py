from django import forms
from django.contrib import admin
from django.contrib.admin import widgets

from ..camunda.utils import get_processes
from .models import Department, Process


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        "camunda_id",
        "department",
        "description",
    )
    list_filter = ("department",)
    ordering = ("department", "camunda_id")
    search_fields = ("camunda_id",)
    filter_horizontal = (
        "other_departments",
        "initiating_processes",
        "applications",
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'camunda_id':
            processes = get_processes()

            choices = [
                (
                    process["id"],
                    f"{process['name']} - {process['version']}",
                )
                for process in processes
            ]

            return forms.ChoiceField(
                label=db_field.verbose_name.capitalize(),
                widget=widgets.AdminRadioSelect(),
                choices=choices,
                required=False,
                help_text=db_field.help_text,
            )

        return super().formfield_for_dbfield(db_field, request, **kwargs)
