from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProcessStatusChoices(models.TextChoices):
    active = "active", _("Active")
    deactivated = "deactivated", _("Deactivated")
    historical = "historical", _("Historical")


class RiskLevels(models.TextChoices):
    high = "high", _("High risk")
    low = "low", _("Low risk")


class StorageTypes(models.TextChoices):
    digital = "digital", _("Digital")
    analogue = "analogue", _("Analogue")
