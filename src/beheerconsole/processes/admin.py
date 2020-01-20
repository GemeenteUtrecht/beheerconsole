from itertools import groupby

from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

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
        "name",
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
    fieldsets = (
        (None, {"fields": ("name", "description", "department", "other_departments",)}),
        (_("Relations"), {"fields": ("initiating_processes", "applications")}),
        (_("Process engine"), {"fields": ("camunda_id",)}),
        (
            _("Systematic overview"),
            {
                "fields": (
                    "personal_data",
                    "process_status",
                    "deactivation_date",
                    "risk_level",
                )
            },
        ),
        (_("Zaakgericht werken"), {"fields": ("zaaktype",)}),
        (_("Misc3"), {"fields": ()}),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "camunda_id":
            processes = get_processes()
            # Camunda versions by key - not name. The same key can have different names
            processes_by_name = groupby(processes, lambda x: x["key"])

            choices = [
                (
                    format_html(_("Process: <code>{key}</code>"), key=key),
                    [
                        (
                            process["id"],
                            _("{name} (version {version})").format(**process),
                        )
                        for process in processes
                    ],
                )
                for key, processes in processes_by_name
            ]

            return forms.ChoiceField(
                label=db_field.verbose_name.capitalize(),
                widget=widgets.AdminRadioSelect(),
                choices=choices,
                required=False,
                help_text=db_field.help_text,
            )

        return super().formfield_for_dbfield(db_field, request, **kwargs)
