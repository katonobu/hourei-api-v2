# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    LAWS = "/laws"
    LAW_REVISIONS_LAW_ID_OR_NUM = "/law_revisions/{law_id_or_num}"
    LAW_DATA_LAW_ID_OR_NUM_OR_REVISION_ID = "/law_data/{law_id_or_num_or_revision_id}"
    ATTACHMENT_LAW_REVISION_ID = "/attachment/{law_revision_id}"
    KEYWORD = "/keyword"
    LAW_FILE_FILE_TYPE_LAW_ID_OR_NUM_OR_REVISION_ID = "/law_file/{file_type}/{law_id_or_num_or_revision_id}"
