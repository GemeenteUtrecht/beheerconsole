from django.contrib import admin

from .models import DataSubject, Record


class DataSubjectInline(admin.TabularInline):
    model = DataSubject
    extra = 0


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "logrecord_id",
        "created",
        "direction",
        "src_organization",
        "dest_organization",
        "service_name",
    )
    list_filter = (
        "src_organization",
        "dest_organization",
        "service_name",
    )
    date_hierarchy = "created"
    search_fields = ("logrecord_id",)
    inlines = [DataSubjectInline]

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False
