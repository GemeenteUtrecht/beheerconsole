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
        "name",
        "department",
        "description",
    )
    list_filter = ("department",)
    ordering = ("department", "name")
    search_fields = ("name",)
    filter_horizontal = (
        "other_departments",
        "initiating_processes",
        "applications",
    )
