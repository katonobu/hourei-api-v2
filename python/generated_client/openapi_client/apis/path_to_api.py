import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.laws import Laws
from openapi_client.apis.paths.law_revisions_law_id_or_num import LawRevisionsLawIdOrNum
from openapi_client.apis.paths.law_data_law_id_or_num_or_revision_id import LawDataLawIdOrNumOrRevisionId
from openapi_client.apis.paths.attachment_law_revision_id import AttachmentLawRevisionId
from openapi_client.apis.paths.keyword import Keyword
from openapi_client.apis.paths.law_file_file_type_law_id_or_num_or_revision_id import LawFileFileTypeLawIdOrNumOrRevisionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.LAWS: Laws,
        PathValues.LAW_REVISIONS_LAW_ID_OR_NUM: LawRevisionsLawIdOrNum,
        PathValues.LAW_DATA_LAW_ID_OR_NUM_OR_REVISION_ID: LawDataLawIdOrNumOrRevisionId,
        PathValues.ATTACHMENT_LAW_REVISION_ID: AttachmentLawRevisionId,
        PathValues.KEYWORD: Keyword,
        PathValues.LAW_FILE_FILE_TYPE_LAW_ID_OR_NUM_OR_REVISION_ID: LawFileFileTypeLawIdOrNumOrRevisionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.LAWS: Laws,
        PathValues.LAW_REVISIONS_LAW_ID_OR_NUM: LawRevisionsLawIdOrNum,
        PathValues.LAW_DATA_LAW_ID_OR_NUM_OR_REVISION_ID: LawDataLawIdOrNumOrRevisionId,
        PathValues.ATTACHMENT_LAW_REVISION_ID: AttachmentLawRevisionId,
        PathValues.KEYWORD: Keyword,
        PathValues.LAW_FILE_FILE_TYPE_LAW_ID_OR_NUM_OR_REVISION_ID: LawFileFileTypeLawIdOrNumOrRevisionId,
    }
)
