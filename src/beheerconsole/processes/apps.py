from django.apps import AppConfig

from zgw_consumers.client import get_client_class


class ProcessesConfig(AppConfig):
    name = "beheerconsole.processes"

    def ready(self):
        Client = get_client_class()
        Client.load_config(
            selectielijst={
                "scheme": "https",
                "host": "referentielijsten-api.vng.cloud",
            }
        )
