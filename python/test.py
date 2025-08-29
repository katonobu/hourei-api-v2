import sys
import os

# generated_client ディレクトリをモジュール検索パスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated_client')))

import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
from openapi_client.model.law_data_response import LawDataResponse
from openapi_client.model.response_format import ResponseFormat
from pprint import pprint
# Defining the host is optional and defaults to https://laws.e-gov.go.jp/api/2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://laws.e-gov.go.jp/api/2"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = laws_api_api.LawsApiApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'law_id_or_num_or_revision_id': "129AC0000000089",
    }
    query_params = {
        'law_full_text_format':'xml',
    }
    try:
        # 法令本文取得API
        api_response = api_instance.get_law_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_law_data: %s\n" % e)


    exit(1)
    # example passing only optional values
    path_params = {
        'law_id_or_num_or_revision_id': "law_id_or_num_or_revision_id_example",
    }
    query_params = {
        'law_full_text_format': None,
        'asof': "1970-01-01",
        'elm': None,
        'omit_amendment_suppl_provision': True,
        'include_attached_file_content': True,
        'response_format': None,
    }
    try:
        # 法令本文取得API
        api_response = api_instance.get_law_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_law_data: %s\n" % e)
