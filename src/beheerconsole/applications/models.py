from django.db import models
from django.utils.translation import ugettext_lazy as _


class Application(models.Model):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(
        _("description"),
        blank=True,
        help_text=_(
            "A description of the application - what does it do, when should you use it..."
        ),
    )
    url = models.URLField(
        _("url"),
        blank=True,
        help_text=_("URL to the application - preferably a home page or similar."),
    )
    admin_url = models.URLField(
        _("admin url"),
        blank=True,
        help_text=_("URL to the application administrative interface."),
    )
    vendor = models.CharField(
        _("vendor"),
        max_length=255,
        help_text=_("Software vendor - who built the appliation and/or maintains it?"),
    )
    repository_url = models.URLField(
        _("repository URL"),
        blank=True,
        help_text=_("URL to the code repository, e.g. Github, Gitlab, Bitbucket..."),
    )
    # relations
    layer = models.ForeignKey(
        "Layer", on_delete=models.CASCADE,
        related_name="applications",
        verbose_name=_("layer"),
        help_text=_("The layer of the application."),
    )

    class Meta:
        verbose_name = _("application")
        verbose_name_plural = _("applications")

    def __str__(self):
        return self.name


class Layer(models.Model):
    tier = models.PositiveSmallIntegerField(_("tier"), help_text=_("The tier number of the layer"))
    description = models.TextField(
        _("description"), blank=True,
        help_text="a description of the layer - what is it aimed for... "
    )

    def __str__(self):
        return f"Layer {self.tier}"
