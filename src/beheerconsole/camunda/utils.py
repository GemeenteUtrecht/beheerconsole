from django_camunda.client import get_client_class

from .models import CamundaBasicAuthConfig


def get_processes() -> list:
    client = get_client_class()(config=CamundaBasicAuthConfig.get_solo())
    response = client.request(
        "process-definition",
        params={"sortBy": "name", "sortOrder": "asc"},
    )
    return response
