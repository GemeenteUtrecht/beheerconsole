from django.contrib import admin

from django_camunda.models import CamundaConfig
from solo.admin import SingletonModelAdmin

from .models import CamundaBasicAuthConfig


@admin.register(CamundaBasicAuthConfig)
class CamundaBasicAuthConfigAdmin(SingletonModelAdmin):
    readonly_fields = ("auth_header",)


admin.site.unregister(CamundaConfig)
