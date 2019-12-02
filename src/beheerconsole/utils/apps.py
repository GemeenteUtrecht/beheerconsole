from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "beheerconsole.utils"

    def ready(self):
        from . import checks  # noqa
