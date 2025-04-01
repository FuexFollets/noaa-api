"""
This type stub file was generated by pyright.
"""

from typing import NotRequired, TypedDict

class ResultSetJSON(TypedDict):
    offset: int
    count: int
    limit: int
    ...


class MetadataJSON(TypedDict):
    resultset: ResultSetJSON
    ...


class RateLimitJSON(TypedDict):
    status: str
    message: str
    ...


class DatasetIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datasets/{id}'
    """
    mindate: str
    maxdate: str
    name: str
    datacoverage: float | int
    id: str
    ...


class DatasetJSON(TypedDict):
    """
    JSON Subcomponent for endpoint '/datasets'
    """
    uid: str
    mindate: str
    maxdate: str
    name: str
    datacoverage: float | int
    id: str
    ...


class DatasetsJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datasets'
    """
    metadata: MetadataJSON
    results: list[DatasetJSON]
    ...


class DatacategoryIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datacategories/{id}'
    """
    name: str
    id: str
    ...


class DatacategoriesJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datacategories'
    """
    metadata: MetadataJSON
    results: list[DatacategoryIDJSON]
    ...


class DatatypeIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datatypes/{id}'
    """
    mindate: str
    maxdate: str
    datacoverage: float | int
    id: str
    ...


class DatatypeJSON(TypedDict):
    """
    JSON Subcomponent for endpoint '/datatypes'
    """
    mindate: str
    maxdate: str
    name: str
    datacoverage: float | int
    id: str
    ...


class DatatypesJSON(TypedDict):
    """
    Full JSON Response for endpoint '/datatypes'
    """
    metadata: MetadataJSON
    results: list[DatatypeJSON]
    ...


class LocationcategoryIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/locationcategories/{id}'
    """
    name: str
    id: str
    ...


class LocationcategoriesJSON(TypedDict):
    """
    Full JSON Response for endpoint '/locationcategories'
    """
    metadata: MetadataJSON
    results: list[LocationcategoryIDJSON]
    ...


class LocationIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/locations/{id}'
    """
    mindate: str
    maxdate: str
    name: str
    datacoverage: float | int
    id: str
    ...


class LocationsJSON(TypedDict):
    """
    Full JSON Response for endpoint '/locations'
    """
    metadata: MetadataJSON
    results: list[LocationIDJSON]
    ...


class StationIDJSON(TypedDict):
    """
    Full JSON Response for endpoint '/stations/{id}'
    """
    elevation: float
    mindate: str
    maxdate: str
    latitude: float
    name: str
    datacoverage: float | int
    id: str
    elevationUnit: str
    longitude: float
    ...


class StationsJSON(TypedDict):
    """
    Full JSON Response for endpoint '/stations'
    """
    metadata: MetadataJSON
    results: list[StationIDJSON]
    ...


class DatapointJSON(TypedDict):
    """
    JSON Subcomponent for endpoint 'data?datasetid=YOUR_DATASETID'
    """
    date: str
    datatype: str
    station: str
    attributes: NotRequired[str]
    value: float | int
    ...


class DataJSON(TypedDict):
    """
    Full JSON Response for endpoint 'data?datasetid=YOUR_DATASETID'
    """
    metadata: MetadataJSON
    results: list[DatapointJSON]
    ...


