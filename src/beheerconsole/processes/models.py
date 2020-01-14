"""
Model how processes and applications are intertwined.

The process is the core object - a process starts and ends and can span
other processes or lead to other processes being started. Process
responsibility is supervised by a department, but other departments *may*
be involved in bringing the process to an end.

Applications are actual software applications that *may* assist in bringing
a process to an end. Not all applications are used for all processes - we can
create an overview of which apps are relevant for processes and vice versa.

The applications app relates back to processes.
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    name = models.CharField(_("name"), max_length=255)
    contact_details = models.TextField(
        _("contact details"),
        blank=True,
        help_text=_("Contact details for the responsible(s) of the department."),
    )

    class Meta:
        verbose_name = _("department")
        verbose_name_plural = _("departments")

    def __str__(self):
        return self.name


class Process(models.Model):
    """
    Represent a process as practiced by the municipality.

    Contains relations to which applications are involved and generally useful
    information.
    """

    camunda_id = models.CharField(
        _("camunda_id"), max_length=255, help_text=_("process-definition id in Camunda")
    )
    description = models.TextField(
        _("description"),
        blank=True,
        help_text=_("Extended description of the process."),
    )
    department = models.ForeignKey(
        "Department",
        on_delete=models.PROTECT,
        related_name="owned_processes",
        verbose_name=_("department"),
        help_text=_("The department responsible for this process."),
    )
    other_departments = models.ManyToManyField(
        "Department",
        blank=True,
        related_name="involved_in",
        verbose_name=_("other departments"),
        help_text=_("Other departments that may play a role in this process"),
    )

    # relations
    initiating_processes = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="initiates",
        verbose_name=_("initiating processes"),
        help_text=_(
            "The set of processes that may lead to this process being started."
        ),
    )
    applications = models.ManyToManyField(
        "applications.Application",
        blank=True,
        related_name="processes",
        help_text=_("Set of applications used to handle this process"),
    )

    class Meta:
        verbose_name = _("process")
        verbose_name_plural = _("processes")

    def __str__(self):
        return self.name

    @property
    def applications_with_layers(self):
        apps = [{"layer": app.layer, "application": app} for app in self.applications.order_by("-layer")]
        return apps

    @property
    def name(self):
        if self.camunda_id:
            return self.camunda_id.split(':')[0]
        return ''

    @property
    def version(self):
        if self.camunda_id:
            return self.camunda_id.split(':')[1]
        return ''
