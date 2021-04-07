from zgw_consumers.api_models.catalogi import ResultaatType, ZaakType
from zgw_consumers.api_models.selectielijst import ProcesType, Resultaat
from zgw_consumers.models import Service


def load_zaaktype(url: str) -> ZaakType:
    client = Service.objects.get_client_for(url)
    Client = client.__class__
    api_data = client.retrieve("zaaktype", url=url)

    # TODO: automate resolution
    selectielijst_client = Client("selectielijst")
    procestype_data = selectielijst_client.retrieve(
        "procestype", url=api_data["selectielijstProcestype"]
    )
    api_data["selectielijstProcestype"] = ProcesType.from_raw(procestype_data)

    zaaktype = ZaakType.from_raw(api_data)
    zaaktype.concept = api_data["concept"]

    # fetch resultaattypen
    resultaattypen_data = client.list(
        "resultaattype",
        query_params={
            "zaaktype": url,
        },
    )["results"]

    resultaattypen = [ResultaatType.from_raw(data) for data in resultaattypen_data]
    for resultaattype in resultaattypen:
        resultaattype.zaaktype = zaaktype

    # fetch resultaten
    _resultaten = selectielijst_client.list(
        "resultaat", query_params={"procesType": procestype_data["url"]}
    )
    assert _resultaten["next"] is None, "Pagination not implemented yet"
    resultaten = {
        _resultaat["url"]: Resultaat.from_raw(_resultaat)
        for _resultaat in _resultaten["results"]
    }
    for resultaattype in resultaattypen:
        resultaattype.selectielijstklasse = resultaten[
            resultaattype.selectielijstklasse
        ]

    zaaktype.resultaattypen = resultaattypen

    return zaaktype
