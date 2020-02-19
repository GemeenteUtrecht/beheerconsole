from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Directions(models.TextChoices):
    IN = "in", _("Incoming")
    OUT = "out", _("Outgoing")


class Record(models.Model):
    id = models.BigAutoField(primary_key=True)
    direction = models.CharField(
        _("direction"), max_length=10, choices=Directions.choices
    )
    created = models.DateTimeField(_("created"))
    src_organization = models.TextField(_("source"))
    dest_organization = models.TextField(_("destination"))
    service_name = models.TextField(_("service name"))
    logrecord_id = models.TextField(_("logrecord ID"))
    data = JSONField(_("data"), blank=True, null=True)

    class Meta:
        managed = False
        db_table = "records"

    def __str__(self):
        return self.logrecord_id


class DataSubject(models.Model):
    id = models.BigAutoField(primary_key=True)
    record = models.ForeignKey("Record", models.CASCADE)
    key = models.CharField(_("key"), max_length=100)
    value = models.CharField(_("value"), max_length=100)

    class Meta:
        managed = False
        db_table = "datasubjects"
        unique_together = (("record", "key"),)
