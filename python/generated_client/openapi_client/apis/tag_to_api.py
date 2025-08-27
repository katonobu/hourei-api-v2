import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.laws_api_api import LawsApiApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.LAWSAPI: LawsApiApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.LAWSAPI: LawsApiApi,
    }
)
