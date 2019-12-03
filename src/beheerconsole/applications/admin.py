from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "vendor")
    list_filter = ("vendor",)
    search_fields = (
        "name",
        "vendor",
    )
