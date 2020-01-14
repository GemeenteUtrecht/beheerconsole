from django.contrib import admin

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
