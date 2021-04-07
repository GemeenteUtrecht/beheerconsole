from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django_activiti.admin import ActivitiFieldsMixin
from django_camunda.admin import CamundaFieldsMixin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from zgw_consumers.admin import ListZaaktypenMixin

from .models import Department, Process, StorageLocation


@admin.register(Department)
class DepartmentAdmin(TreeAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    form = movenodeform_factory(Department)


@admin.register(Process)
class ProcessAdmin(
    CamundaFieldsMixin, ActivitiFieldsMixin, ListZaaktypenMixin, admin.ModelAdmin
):
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
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "department",
                    "other_departments",
                )
            },
        ),
        (_("Relations"), {"fields": ("initiating_processes", "applications")}),
        (
            _("Process engine"),
            {
                "fields": (
                    "camunda_id",
                    "activiti_id",
                )
            },
        ),
        (
            _("Systematic overview"),
            {
                "fields": (
                    "personal_data",
                    "process_status",
                    "deactivation_date",
                    "risk_level",
                    "location_digital",
                    "location_analogue",
                    "zaaktype_owner",
                )
            },
        ),
        (_("Zaakgericht werken"), {"fields": ("zaaktype",)}),
    )
    raw_id_fields = (
        "department",
        "zaaktype_owner",
    )
    zaaktype_fields = ("zaaktype",)


@admin.register(StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):
    list_display = ("name", "storage_type")
    list_filter = ("storage_type",)
    search_fields = ("name",)
    ordering = ("name",)
