import base64

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_camunda.models import CamundaConfig


class CamundaBasicAuthConfig(CamundaConfig):
    username = models.CharField(_("username for BasicAuth"), max_length=150, blank=True)
    password = models.CharField(_("password for BasicAuth"), max_length=150, blank=True)

    def set_auth(self):
        if self.username and not self.auth_header:
            encoded_str = base64.b64encode(f"{self.username}:{self.password}".encode())
            self.auth_header = f"Basic {encoded_str.decode()}"

    def clean(self):
        self.set_auth()
        super().clean()
