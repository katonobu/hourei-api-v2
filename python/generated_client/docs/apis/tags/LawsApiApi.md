<a id="__pageTop"></a>
# openapi_client.apis.tags.laws_api_api.LawsApiApi

All URIs are relative to *https://laws.e-gov.go.jp/api/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attachment**](#get_attachment) | **get** /attachment/{law_revision_id} | 添付ファイル取得API
[**get_keyword**](#get_keyword) | **get** /keyword | キーワード検索API
[**get_law_data**](#get_law_data) | **get** /law_data/{law_id_or_num_or_revision_id} | 法令本文取得API
[**get_law_file**](#get_law_file) | **get** /law_file/{file_type}/{law_id_or_num_or_revision_id} | 法令本文ファイル取得API
[**get_laws**](#get_laws) | **get** /laws | 法令一覧取得API
[**get_revisions**](#get_revisions) | **get** /law_revisions/{law_id_or_num} | 法令履歴一覧取得API

# **get_attachment**
<a id="get_attachment"></a>
> file_type get_attachment(law_revision_id)

添付ファイル取得API

## 概要 > &nbsp;&nbsp;法令履歴ID（`law_revision_id`）を指定必須パラメータとして、法令本文の添付ファイルを取得します。<br> > &nbsp;&nbsp;法令データ上に存在する添付ファイルの拡張子には、`jpg`、`pdf`があります。<br>  > &nbsp;&nbsp;法令本文取得APIのレスポンスデータに含まれる`attached_files_info`のsrc属性（`src`）を指定することで特定の添付ファイルが取得できます。<br> > &nbsp;&nbsp;src属性（`src`）を指定しない場合は、法令本文に含まれる添付ファイルをZip形式で一括取得できます。   ## 補足事項 > &nbsp;&nbsp;src属性（`src`）の指定有無によってレスポンスの動作が異なります。<br>  > &nbsp;&nbsp;src属性（`src`）指定時、 > * &nbsp;&nbsp;SwaggerUIでAPIを実行した場合、`jpg`が返却される場合は画像が表示されます。`pdf`の場合はダウンロードリンクが表示されます。 > * &nbsp;&nbsp;URLを直接入力した場合、`jpg`が返却される場合は画像が表示されます。`pdf`の場合はファイルがダウンロードされます。  > &nbsp;&nbsp;src属性（`src`）未指定時、 > * &nbsp;&nbsp;SwaggerUIでAPIを実行した場合、`jpg`、`pdf`のいずれもダウンロードリンクが表示されます。 > * &nbsp;&nbsp;URLを直接入力した場合、`jpg`、`pdf`のいずれもZip形式でファイルがダウンロードされます。 

### Example

```python
import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
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
        'law_revision_id': "law_revision_id_example",
    }
    query_params = {
    }
    try:
        # 添付ファイル取得API
        api_response = api_instance.get_attachment(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'law_revision_id': "law_revision_id_example",
    }
    query_params = {
        'src': "src_example",
    }
    try:
        # 添付ファイル取得API
        api_response = api_instance.get_attachment(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src | SrcSchema | | optional


# SrcSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_revision_id | LawRevisionIdSchema | | 

# LawRevisionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_attachment.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_attachment.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_attachment.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody

ファイルの内容（バイナリ形式）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | ファイルの内容（バイナリ形式） | 

#### get_attachment.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_attachment.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_keyword**
<a id="get_keyword"></a>
> KeywordResponse get_keyword(keyword)

キーワード検索API

## 概要 > キーワード（`keyword`）を指定必須とし、法令本文内に指定したキーワード（`keyword`）を含む法令を取得します。<br> > 本エンドポイントでは、法令本文（`law_full_text`）を対象に全文検索を行います。<br> > 指定任意のパラメータと組み合わせることで、返却データを絞り込むことができます。  ## 補足事項 > &nbsp;&nbsp;本エンドポイントで返却されるデータの解説は以下のとおりです。  > * `law_info` >> &nbsp;&nbsp;&nbsp;法令番号（`law_num`）や公布日（`promulgation_date`）等、改正履歴に依存しないデータが格納されます。 <br>  > * `revision_info` >> &nbsp;&nbsp;&nbsp;改正後の法令名（`law_title`）や改正法令公布日（`amendment_promulgate_date`）等、改正履歴に依存するデータが格納されます。<br> >> &nbsp;&nbsp;&nbsp;法令の時点（`asof`）を指定した場合はその時点で最新の改正履歴を格納します。<br>  > * ### `sentences` >> &nbsp;&nbsp;キーワード（`keyword`）に該当する法令本文の見出し等の構造（`position`）と条文内容（`text`）が格納されます。 

### Example

```python
import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
from openapi_client.model.keyword_response import KeywordResponse
from openapi_client.model.category_cd import CategoryCd
from openapi_client.model.law_num_type import LawNumType
from openapi_client.model.law_num_era import LawNumEra
from openapi_client.model.response_format import ResponseFormat
from openapi_client.model.law_type import LawType
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
    query_params = {
        'keyword': "keyword_example",
    }
    try:
        # キーワード検索API
        api_response = api_instance.get_keyword(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_keyword: %s\n" % e)

    # example passing only optional values
    query_params = {
        'keyword': "keyword_example",
        'law_num': "law_num_example",
        'law_num_era': LawNumEra("Meiji"),
        'law_num_num': "law_num_num_example",
        'law_num_type': LawNumType("Constitution"),
        'law_num_year': 1,
        'law_type': [
        LawType("Constitution")
    ],
        'asof': "1970-01-01",
        'category_cd': [
        CategoryCd("001")
    ],
        'promulgation_date_from': "1970-01-01",
        'promulgation_date_to': "1970-01-01",
        'limit': 1,
        'offset': 1,
        'order': "order_example",
        'response_format': None,
        'sentences_limit': 1,
        'sentence_text_size': 1,
        'highlight_tag': "highlight_tag_example",
    }
    try:
        # キーワード検索API
        api_response = api_instance.get_keyword(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_keyword: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
keyword | KeywordSchema | | 
law_num | LawNumSchema | | optional
law_num_era | LawNumEraSchema | | optional
law_num_num | LawNumNumSchema | | optional
law_num_type | LawNumTypeSchema | | optional
law_num_year | LawNumYearSchema | | optional
law_type | LawTypeSchema | | optional
asof | AsofSchema | | optional
category_cd | CategoryCdSchema | | optional
promulgation_date_from | PromulgationDateFromSchema | | optional
promulgation_date_to | PromulgationDateToSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
order | OrderSchema | | optional
response_format | ResponseFormatSchema | | optional
sentences_limit | SentencesLimitSchema | | optional
sentence_text_size | SentenceTextSizeSchema | | optional
highlight_tag | HighlightTagSchema | | optional


# KeywordSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumEraSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LawNumEra**](../../models/LawNumEra.md) |  | 


# LawNumNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LawNumType**](../../models/LawNumType.md) |  | 


# LawNumYearSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LawTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LawType**]({{complexTypePrefix}}LawType.md) | [**LawType**]({{complexTypePrefix}}LawType.md) | [**LawType**]({{complexTypePrefix}}LawType.md) |  | 

# AsofSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# CategoryCdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) |  | 

# PromulgationDateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# PromulgationDateToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResponseFormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResponseFormat]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) |  | 

# SentencesLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SentenceTextSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# HighlightTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_keyword.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_keyword.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_keyword.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_keyword.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**KeywordResponse**](../../models/KeywordResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**KeywordResponse**](../../models/KeywordResponse.md) |  | 


#### get_keyword.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_keyword.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_law_data**
<a id="get_law_data"></a>
> LawDataResponse get_law_data(law_id_or_num_or_revision_id)

法令本文取得API

## 概要 > &nbsp;&nbsp;法令ID（`law_id`）、法令番号（`law_num`）、法令履歴ID（`law_revision_id`）のいずれかを指定必須として、指定した法令の本文を取得します。<br> > * &nbsp;&nbsp;法令ID（`law_id`）、法令番号（`law_num`）を指定した場合は、現時点で最新のリビジョンの本文を取得します。<br> > * &nbsp;&nbsp;法令履歴ID（`law_revision_id`）を指定した場合は、該当するリビジョンの本文を取得します。<br> > * &nbsp;&nbsp;上記の指定必須のパラメータがわからない場合は、法令一覧取得APIで法令名（`law_title`）等を指定してパラメータを調べてください。  >&nbsp;&nbsp;<font color=\"red\"><b>注意：</b><br> >&nbsp;&nbsp;法令本文のデータサイズが大きい場合、エラーが発生することがあります。<br> >&nbsp;&nbsp;エラーが発生した場合は、SwaggerUI以外（Microsoft EdgeやGoogle Chromeといったブラウザで法令APIのURLを直接指定等）で実行してください。</font>   ## 補足事項 > &nbsp;&nbsp;本エンドポイントで返却されるデータの解説は以下のとおりです。<br>  > * `attached_files_info` >>&nbsp;&nbsp;添付ファイルに関するデータが格納されます。   > * `law_info` >>&nbsp;&nbsp;法令番号（`law_num`）や公布日（`promulgation_date`）等、改正履歴に依存しないデータが格納されます。   > * `revision_info` >>&nbsp;&nbsp;改正後の法令名（`law_title`）や改正法令公布日（`amendment_promulgate_date`）等、改正履歴に依存するデータが格納されます。<br> >>&nbsp;&nbsp;法令の時点（`asof`）を指定した場合はその時点で最新の改正履歴を格納します。  > * `law_full_text` >>&nbsp;&nbsp;法令の本文情報が格納されます。<br> >>&nbsp;&nbsp;要素（`elm`）パラメータを指定することで要素を絞り込んで本文を取得することができます。指定方法はSchemasの<a href=\"#model-elm\">`elm`</a>を参照してください。   ## 法令本文のレスポンス形式 > &nbsp;&nbsp;レスポンス形式（`response_format`）を指定することでデータのレスポンス形式をJSON、又はXMLに切り替えることができます。<br> > &nbsp;&nbsp;また、法令本文の形式（`law_full_text_format`）を指定することで法令本文（`law_full_text`）のレスポンス形式を切り替えることができます。  > * レスポンス形式（`response_format`）を`json` 、かつ法令本文（`law_full_text`） を`xml`で指定した場合、法令本文（`law_full_text`）はXML形式で返却されます。<br>  > * レスポンス形式（`response_format`）を`xml`、かつ法令本文（`law_full_text`）を`json`で指定した場合、法令本文（`law_full_text`）はJSON形式で返却されます。<br>  >> <font color=\"red\">上記のように`response_format`と`law_full_text`が異なる場合、`law_full_text`の返却値はBase64でエンコードしておりますので、ご利用の際はBase64でデコードしてください。</font>   ## XMLとJSONの関係性  >> 例）以下のXMLをJSONで表した場合の対応表を以下に記します。<br> >> ### XMLイメージ  >>> <pre><code>&lt;Sentence Num=\"1\" WritingMode=\"vertical\"&gt; &nbsp;&nbsp;この法律は、処分、行政指導及び届出に関する手続並びに命令等を定める手続に関し、・・・ &lt;/Sentence&gt; </code></pre>    >> ### JSONイメージ >>> <pre><code>{ &nbsp;&nbsp;\"tag\": \"Sentence\", &nbsp;&nbsp;\"attr\": { &nbsp;&nbsp;&nbsp;&nbsp;\"Num\": \"1\", &nbsp;&nbsp;&nbsp;&nbsp;\"WritingMode\": \"vertical\" &nbsp;&nbsp;}, &nbsp;&nbsp;\"children\": [ &nbsp;&nbsp;&nbsp;&nbsp;\"この法律は、処分、行政指導及び届出に関する手続並びに命令等を定める手続に関し、・・・\" &nbsp;&nbsp;] } </code></pre>   >> ### XMLとJSONの対応表 >>> <table bgcolor=\"white\" border=\"1\">   <tr bgcolor=\"#DDFFFF\">     <th width=\"10%\">項目名</th>     <th width=\"45%\">XML</th>     <th width=\"45%\">JSON</th>   </tr>   <tr>     <td>タグ</td>     <td>Sentence</td>     <td>\"tag\": \"Sentence\"</td>   </tr>   <tr>     <td>属性</td>     <td>Num=\"1\" WritingMode=\"vertical\"</td>     <td>\"attr\": {\"Num\": \"1\",\"WritingMode\": \"vertical\"}</td>     </tr>   <tr>     <td>子要素</td>     <td>この法律は、処分、行政指導及び届出に関する手続並びに命令等を定める手続に関し、・・・</td>     <td>\"children\": [\"この法律は、処分、行政指導及び届出に関する手続並びに命令等を定める手続に関し、・・・\"]</td>   </tr> </table> 

### Example

```python
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
        'law_id_or_num_or_revision_id': "law_id_or_num_or_revision_id_example",
    }
    query_params = {
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
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_full_text_format | LawFullTextFormatSchema | | optional
asof | AsofSchema | | optional
elm | ElmSchema | | optional
omit_amendment_suppl_provision | OmitAmendmentSupplProvisionSchema | | optional
include_attached_file_content | IncludeAttachedFileContentSchema | | optional
response_format | ResponseFormatSchema | | optional


# LawFullTextFormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | if omitted the server will use the default value of null

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResponseFormat]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) |  | 

# AsofSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# ElmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | str,  | str,  | 指定した法令XMLの要素に該当する法令本文を取得することができます。&lt;br&gt; * 要素を組み合わせる場合は、&#x60;-&#x60;（半角ハイフン）で要素を結合してください。&lt;br&gt; &gt; （例：本則第１項 &#x60;MainProvision-Paragraph_1&#x60;） * 下記の表に要素毎の一覧と指定方法を記載しております。 * 表に掲載している要素は一例であり、elmで取得可能な要素の詳細は&lt;a href&#x3D;\&quot;https://laws.e-gov.go.jp/docs/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;法令データ ドキュメンテーション&lt;/a&gt;を参照してください。&lt;br&gt;  &lt;font color&#x3D;\&quot;red\&quot;&gt; 補足：&lt;br&gt; &amp;nbsp;&amp;nbsp;指定した要素内に他要素がある場合は、他要素の情報も取得されます。&lt;br&gt; &amp;nbsp;&amp;nbsp;例えば、&#x60;MainProvision-Paragraph[1]&#x60;を指定した場合は、指定された&#x60;Paragraph&#x60;要素内に&#x60;FigStruct&#x60;要素が存在していると&#x60;FigStruct&#x60;情報も含めて取得されます。 &lt;/font&gt;  &lt;table bgcolor&#x3D;\&quot;white\&quot; border&#x3D;\&quot;1\&quot;&gt;      &lt;tr bgcolor&#x3D;\&quot;#DDFFFF\&quot;&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;法令XML要素&lt;/th&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;要素の意味&lt;/th&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;指定例&lt;/th&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; LawNum &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 法令番号 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; LawNum[1]&lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; LawTitle &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 題名 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; LawTitle[1]&lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; EnactStatement &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 制定文 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; EnactStatement[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; TOC &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 目次 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; TOC[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Preamble &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 前文 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Preamble[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; MainProvision &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 本則 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; MainProvision[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Part &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 編 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Part_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Chapter &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 章 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Chapter_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Section &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 節 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Section_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Subsection &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 款 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Subsection_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Division &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 目 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Division_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Article &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 条 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Article_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Paragraph &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 項 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Paragraph_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Item &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 号 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Item_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Subitem1 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 号細分 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Subitem1_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; SupplProvision &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 附則 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; SupplProvision[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxTable &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別表 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxTable[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxStyle &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別記様式 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxStyle[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxFormat &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別記書式 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxFormat[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Appdx &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 付録 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Appdx[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxFig &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別図 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxFig[1] &lt;/td&gt;      &lt;/tr&gt;    &lt;/table&gt;  | 

# all_of_0

指定した法令XMLの要素に該当する法令本文を取得することができます。<br> * 要素を組み合わせる場合は、`-`（半角ハイフン）で要素を結合してください。<br> > （例：本則第１項 `MainProvision-Paragraph_1`） * 下記の表に要素毎の一覧と指定方法を記載しております。 * 表に掲載している要素は一例であり、elmで取得可能な要素の詳細は<a href=\"https://laws.e-gov.go.jp/docs/\" target=\"_blank\">法令データ ドキュメンテーション</a>を参照してください。<br>  <font color=\"red\"> 補足：<br> &nbsp;&nbsp;指定した要素内に他要素がある場合は、他要素の情報も取得されます。<br> &nbsp;&nbsp;例えば、`MainProvision-Paragraph[1]`を指定した場合は、指定された`Paragraph`要素内に`FigStruct`要素が存在していると`FigStruct`情報も含めて取得されます。 </font>  <table bgcolor=\"white\" border=\"1\">      <tr bgcolor=\"#DDFFFF\">        <th width=\"20%\">法令XML要素</th>        <th width=\"20%\">要素の意味</th>        <th width=\"20%\">指定例</th>      </tr>      <tr>        <td>&nbsp; LawNum </td>        <td>&nbsp; 法令番号 </td>        <td>&nbsp; LawNum[1]</td>      </tr>      <tr>        <td>&nbsp; LawTitle </td>        <td>&nbsp; 題名 </td>        <td>&nbsp; LawTitle[1]</td>      </tr>      <tr>        <td>&nbsp; EnactStatement </td>        <td>&nbsp; 制定文 </td>        <td>&nbsp; EnactStatement[1] </td>      </tr>      <tr>        <td>&nbsp; TOC </td>        <td>&nbsp; 目次 </td>        <td>&nbsp; TOC[1] </td>      </tr>      <tr>        <td>&nbsp; Preamble </td>        <td>&nbsp; 前文 </td>        <td>&nbsp; Preamble[1] </td>      </tr>      <tr>        <td>&nbsp; MainProvision </td>        <td>&nbsp; 本則 </td>        <td>&nbsp; MainProvision[1] </td>      </tr>      <tr>        <td>&nbsp; Part </td>        <td>&nbsp; 編 </td>        <td>&nbsp; Part_1 </td>      </tr>      <tr>        <td>&nbsp; Chapter </td>        <td>&nbsp; 章 </td>        <td>&nbsp; Chapter_1 </td>      </tr>      <tr>        <td>&nbsp; Section </td>        <td>&nbsp; 節 </td>        <td>&nbsp; Section_1 </td>      </tr>      <tr>        <td>&nbsp; Subsection </td>        <td>&nbsp; 款 </td>        <td>&nbsp; Subsection_1 </td>      </tr>      <tr>        <td>&nbsp; Division </td>        <td>&nbsp; 目 </td>        <td>&nbsp; Division_1 </td>      </tr>      <tr>        <td>&nbsp; Article </td>        <td>&nbsp; 条 </td>        <td>&nbsp; Article_1 </td>      </tr>      <tr>        <td>&nbsp; Paragraph </td>        <td>&nbsp; 項 </td>        <td>&nbsp; Paragraph_1 </td>      </tr>      <tr>        <td>&nbsp; Item </td>        <td>&nbsp; 号 </td>        <td>&nbsp; Item_1 </td>      </tr>      <tr>        <td>&nbsp; Subitem1 </td>        <td>&nbsp; 号細分 </td>        <td>&nbsp; Subitem1_1 </td>      </tr>      <tr>        <td>&nbsp; SupplProvision </td>        <td>&nbsp; 附則 </td>        <td>&nbsp; SupplProvision[1] </td>      </tr>      <tr>        <td>&nbsp; AppdxTable </td>        <td>&nbsp; 別表 </td>        <td>&nbsp; AppdxTable[1] </td>      </tr>      <tr>        <td>&nbsp; AppdxStyle </td>        <td>&nbsp; 別記様式 </td>        <td>&nbsp; AppdxStyle[1] </td>      </tr>      <tr>        <td>&nbsp; AppdxFormat </td>        <td>&nbsp; 別記書式 </td>        <td>&nbsp; AppdxFormat[1] </td>      </tr>      <tr>        <td>&nbsp; Appdx </td>        <td>&nbsp; 付録 </td>        <td>&nbsp; Appdx[1] </td>      </tr>      <tr>        <td>&nbsp; AppdxFig </td>        <td>&nbsp; 別図 </td>        <td>&nbsp; AppdxFig[1] </td>      </tr>    </table> 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | 指定した法令XMLの要素に該当する法令本文を取得することができます。&lt;br&gt; * 要素を組み合わせる場合は、&#x60;-&#x60;（半角ハイフン）で要素を結合してください。&lt;br&gt; &gt; （例：本則第１項 &#x60;MainProvision-Paragraph_1&#x60;） * 下記の表に要素毎の一覧と指定方法を記載しております。 * 表に掲載している要素は一例であり、elmで取得可能な要素の詳細は&lt;a href&#x3D;\&quot;https://laws.e-gov.go.jp/docs/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;法令データ ドキュメンテーション&lt;/a&gt;を参照してください。&lt;br&gt;  &lt;font color&#x3D;\&quot;red\&quot;&gt; 補足：&lt;br&gt; &amp;nbsp;&amp;nbsp;指定した要素内に他要素がある場合は、他要素の情報も取得されます。&lt;br&gt; &amp;nbsp;&amp;nbsp;例えば、&#x60;MainProvision-Paragraph[1]&#x60;を指定した場合は、指定された&#x60;Paragraph&#x60;要素内に&#x60;FigStruct&#x60;要素が存在していると&#x60;FigStruct&#x60;情報も含めて取得されます。 &lt;/font&gt;  &lt;table bgcolor&#x3D;\&quot;white\&quot; border&#x3D;\&quot;1\&quot;&gt;      &lt;tr bgcolor&#x3D;\&quot;#DDFFFF\&quot;&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;法令XML要素&lt;/th&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;要素の意味&lt;/th&gt;        &lt;th width&#x3D;\&quot;20%\&quot;&gt;指定例&lt;/th&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; LawNum &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 法令番号 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; LawNum[1]&lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; LawTitle &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 題名 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; LawTitle[1]&lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; EnactStatement &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 制定文 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; EnactStatement[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; TOC &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 目次 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; TOC[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Preamble &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 前文 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Preamble[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; MainProvision &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 本則 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; MainProvision[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Part &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 編 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Part_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Chapter &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 章 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Chapter_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Section &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 節 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Section_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Subsection &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 款 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Subsection_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Division &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 目 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Division_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Article &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 条 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Article_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Paragraph &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 項 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Paragraph_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Item &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 号 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Item_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Subitem1 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 号細分 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Subitem1_1 &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; SupplProvision &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 附則 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; SupplProvision[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxTable &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別表 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxTable[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxStyle &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別記様式 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxStyle[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxFormat &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別記書式 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxFormat[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; Appdx &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 付録 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; Appdx[1] &lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;        &lt;td&gt;&amp;nbsp; AppdxFig &lt;/td&gt;        &lt;td&gt;&amp;nbsp; 別図 &lt;/td&gt;        &lt;td&gt;&amp;nbsp; AppdxFig[1] &lt;/td&gt;      &lt;/tr&gt;    &lt;/table&gt;  | 

# OmitAmendmentSupplProvisionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# IncludeAttachedFileContentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ResponseFormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | if omitted the server will use the default value of null

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResponseFormat]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_id_or_num_or_revision_id | LawIdOrNumOrRevisionIdSchema | | 

# LawIdOrNumOrRevisionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_law_data.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_law_data.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_law_data.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_law_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LawDataResponse**](../../models/LawDataResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**LawDataResponse**](../../models/LawDataResponse.md) |  | 


#### get_law_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_law_data.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_law_file**
<a id="get_law_file"></a>
> file_type get_law_file(law_id_or_num_or_revision_id_file_type)

法令本文ファイル取得API

## 概要 > &nbsp;&nbsp;法令ID（`law_id`）、法令番号（`law_num`）、法令履歴ID（`law_revision_id`）のいずれかと、ファイル種別（`file_type`）を指定必須として、<br> > &nbsp;&nbsp;法令本文をダウンロードすることができます。 

### Example

```python
import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
from openapi_client.model.file_type import FileType
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
        'law_id_or_num_or_revision_id': "law_id_or_num_or_revision_id_example",
        'file_type': None,
    }
    query_params = {
    }
    try:
        # 法令本文ファイル取得API
        api_response = api_instance.get_law_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_law_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'law_id_or_num_or_revision_id': "law_id_or_num_or_revision_id_example",
        'file_type': None,
    }
    query_params = {
        'asof': "1970-01-01",
    }
    try:
        # 法令本文ファイル取得API
        api_response = api_instance.get_law_file(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_law_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
asof | AsofSchema | | optional


# AsofSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_id_or_num_or_revision_id | LawIdOrNumOrRevisionIdSchema | | 
file_type | FileTypeSchema | | 

# LawIdOrNumOrRevisionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FileTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[FileType]({{complexTypePrefix}}FileType.md) | [**FileType**]({{complexTypePrefix}}FileType.md) | [**FileType**]({{complexTypePrefix}}FileType.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_law_file.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_law_file.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_law_file.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_law_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody

法令本文ファイル（バイナリ形式）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | 法令本文ファイル（バイナリ形式） | 

#### get_law_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_law_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_laws**
<a id="get_laws"></a>
> LawsResponse get_laws()

法令一覧取得API

## 概要 > &nbsp;&nbsp;指定条件に該当する法令データが返却されます。<br> > &nbsp;&nbsp;例えば、法令名（`law_title`）を指定した場合、指定した法令名を含む法令データが返却されます。<br> > &nbsp;&nbsp;法令種別（`law_type`）を指定した場合、指定した法令種別の法令データが返却されます。<br> > &nbsp;&nbsp;指定必須のパラメータはありません。また、全パラメータを組み合わせる必要もありません。<br> > &nbsp;&nbsp;必要なパラメータを組み合わせて法令データを取得することができます。<br>   ## 補足事項 > &nbsp;&nbsp;本エンドポイントは、指定条件に該当するデータを`laws`に格納します。<br> > &nbsp;&nbsp;`laws`配下に格納されるデータの解説は以下のとおりです。<br>  > * `law_info` >> &nbsp;&nbsp;&nbsp;法令番号（`law_num`）や公布日（`promulgation_date`）等、改正履歴に依存しないデータが格納されます。 <br>  > * `revision_info` >> &nbsp;&nbsp;&nbsp;改正後の法令名（`law_title`）や改正法令公布日（`amendment_promulgate_date`）等、改正履歴に依存するデータが格納されます。<br> >> &nbsp;&nbsp;&nbsp;法令の時点（`asof`）を指定した場合はその時点で最新の改正履歴を格納します。<br>  > * `current_revision_info` >>  &nbsp;&nbsp;&nbsp;法令の時点（`asof`）等の指定にかかわらず、現時点で最新の改正履歴を格納します。<br> 

### Example

```python
import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
from openapi_client.model.mission import Mission
from openapi_client.model.category_cd import CategoryCd
from openapi_client.model.law_num_type import LawNumType
from openapi_client.model.law_num_era import LawNumEra
from openapi_client.model.response_format import ResponseFormat
from openapi_client.model.law_type import LawType
from openapi_client.model.laws_response import LawsResponse
from openapi_client.model.repeal_status import RepealStatus
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

    # example passing only optional values
    query_params = {
        'law_id': "law_id_example",
        'law_num': "law_num_example",
        'law_num_era': LawNumEra("Meiji"),
        'law_num_num': "law_num_num_example",
        'law_num_type': LawNumType("Constitution"),
        'law_num_year': 1,
        'law_title': "law_title_example",
        'law_title_kana': "law_title_kana_example",
        'law_type': [
        LawType("Constitution")
    ],
        'amendment_law_id': "amendment_law_id_example",
        'asof': "1970-01-01",
        'category_cd': [
        CategoryCd("001")
    ],
        'mission': [
        Mission("New")
    ],
        'omit_current_revision_info': True,
        'promulgation_date_from': "1970-01-01",
        'promulgation_date_to': "1970-01-01",
        'repeal_status': [
        RepealStatus("None")
    ],
        'limit': 1,
        'offset': 1,
        'order': "order_example",
        'response_format': None,
    }
    try:
        # 法令一覧取得API
        api_response = api_instance.get_laws(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_laws: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_id | LawIdSchema | | optional
law_num | LawNumSchema | | optional
law_num_era | LawNumEraSchema | | optional
law_num_num | LawNumNumSchema | | optional
law_num_type | LawNumTypeSchema | | optional
law_num_year | LawNumYearSchema | | optional
law_title | LawTitleSchema | | optional
law_title_kana | LawTitleKanaSchema | | optional
law_type | LawTypeSchema | | optional
amendment_law_id | AmendmentLawIdSchema | | optional
asof | AsofSchema | | optional
category_cd | CategoryCdSchema | | optional
mission | MissionSchema | | optional
omit_current_revision_info | OmitCurrentRevisionInfoSchema | | optional
promulgation_date_from | PromulgationDateFromSchema | | optional
promulgation_date_to | PromulgationDateToSchema | | optional
repeal_status | RepealStatusSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional
order | OrderSchema | | optional
response_format | ResponseFormatSchema | | optional


# LawIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumEraSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LawNumEra**](../../models/LawNumEra.md) |  | 


# LawNumNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawNumTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**LawNumType**](../../models/LawNumType.md) |  | 


# LawNumYearSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LawTitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawTitleKanaSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LawType**]({{complexTypePrefix}}LawType.md) | [**LawType**]({{complexTypePrefix}}LawType.md) | [**LawType**]({{complexTypePrefix}}LawType.md) |  | 

# AmendmentLawIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AsofSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# CategoryCdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) |  | 

# MissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Mission**]({{complexTypePrefix}}Mission.md) | [**Mission**]({{complexTypePrefix}}Mission.md) | [**Mission**]({{complexTypePrefix}}Mission.md) |  | 

# OmitCurrentRevisionInfoSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PromulgationDateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# PromulgationDateToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# RepealStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) | [**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) | [**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResponseFormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResponseFormat]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_laws.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_laws.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_laws.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_laws.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LawsResponse**](../../models/LawsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**LawsResponse**](../../models/LawsResponse.md) |  | 


#### get_laws.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_laws.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_revisions**
<a id="get_revisions"></a>
> LawRevisionsResponse get_revisions(law_id_or_num)

法令履歴一覧取得API

## 概要 > &nbsp;&nbsp;法令ID（`law_id`）又は法令番号（`law_num`）を指定必須として、指定した法令の改正履歴が返却されます。<br> > &nbsp;&nbsp;改正履歴は`revisions`配下に格納されており、上から法令履歴ID（`law_revision_id`）が新しい順で改正履歴が返却されます。<br> > &nbsp;&nbsp;指定任意のパラメータと組み合わせることで、返却データを絞り込むことができます。<br>  ## 補足事項 > &nbsp;&nbsp;本エンドポイントで返却されるデータの解説は以下のとおりです。<br>  > * `law_info` >> &nbsp;&nbsp;&nbsp;法令番号（`law_num`）や公布日（`promulgation_date`）等、改正履歴に依存しない法令データが格納されます。  > * `revisions` >> &nbsp;&nbsp;&nbsp;改正後の法令名（`law_title`）や改正法令公布日（`amendment_promulgate_date`）等、改正履歴に依存する法令データが格納されます。<br> 

### Example

```python
import openapi_client
from openapi_client.apis.tags import laws_api_api
from openapi_client.model.error_info import ErrorInfo
from openapi_client.model.mission import Mission
from openapi_client.model.category_cd import CategoryCd
from openapi_client.model.amendment_type import AmendmentType
from openapi_client.model.response_format import ResponseFormat
from openapi_client.model.current_revision_status import CurrentRevisionStatus
from openapi_client.model.repeal_status import RepealStatus
from openapi_client.model.law_revisions_response import LawRevisionsResponse
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
        'law_id_or_num': "law_id_or_num_example",
    }
    query_params = {
    }
    try:
        # 法令履歴一覧取得API
        api_response = api_instance.get_revisions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_revisions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'law_id_or_num': "law_id_or_num_example",
    }
    query_params = {
        'law_title': "law_title_example",
        'law_title_kana': "law_title_kana_example",
        'amendment_date_from': "1970-01-01",
        'amendment_date_to': "1970-01-01",
        'amendment_law_id': "amendment_law_id_example",
        'amendment_law_num': "amendment_law_num_example",
        'amendment_law_title': "amendment_law_title_example",
        'amendment_law_title_kana': "amendment_law_title_kana_example",
        'amendment_promulgate_date_from': "1970-01-01",
        'amendment_promulgate_date_to': "1970-01-01",
        'amendment_type': [
        AmendmentType("1")
    ],
        'category_cd': [
        CategoryCd("001")
    ],
        'current_revision_status': [
        CurrentRevisionStatus("CurrentEnforced")
    ],
        'mission': [
        Mission("New")
    ],
        'remain_in_force': True,
        'repeal_date_from': "1970-01-01",
        'repeal_date_to': "1970-01-01",
        'repeal_status': [
        RepealStatus("None")
    ],
        'updated_from': "1970-01-01",
        'updated_to': "1970-01-01",
        'response_format': None,
    }
    try:
        # 法令履歴一覧取得API
        api_response = api_instance.get_revisions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LawsApiApi->get_revisions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_title | LawTitleSchema | | optional
law_title_kana | LawTitleKanaSchema | | optional
amendment_date_from | AmendmentDateFromSchema | | optional
amendment_date_to | AmendmentDateToSchema | | optional
amendment_law_id | AmendmentLawIdSchema | | optional
amendment_law_num | AmendmentLawNumSchema | | optional
amendment_law_title | AmendmentLawTitleSchema | | optional
amendment_law_title_kana | AmendmentLawTitleKanaSchema | | optional
amendment_promulgate_date_from | AmendmentPromulgateDateFromSchema | | optional
amendment_promulgate_date_to | AmendmentPromulgateDateToSchema | | optional
amendment_type | AmendmentTypeSchema | | optional
category_cd | CategoryCdSchema | | optional
current_revision_status | CurrentRevisionStatusSchema | | optional
mission | MissionSchema | | optional
remain_in_force | RemainInForceSchema | | optional
repeal_date_from | RepealDateFromSchema | | optional
repeal_date_to | RepealDateToSchema | | optional
repeal_status | RepealStatusSchema | | optional
updated_from | UpdatedFromSchema | | optional
updated_to | UpdatedToSchema | | optional
response_format | ResponseFormatSchema | | optional


# LawTitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LawTitleKanaSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmendmentDateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AmendmentDateToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AmendmentLawIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmendmentLawNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmendmentLawTitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmendmentLawTitleKanaSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AmendmentPromulgateDateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AmendmentPromulgateDateToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# AmendmentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AmendmentType**]({{complexTypePrefix}}AmendmentType.md) | [**AmendmentType**]({{complexTypePrefix}}AmendmentType.md) | [**AmendmentType**]({{complexTypePrefix}}AmendmentType.md) |  | 

# CategoryCdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) | [**CategoryCd**]({{complexTypePrefix}}CategoryCd.md) |  | 

# CurrentRevisionStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CurrentRevisionStatus**]({{complexTypePrefix}}CurrentRevisionStatus.md) | [**CurrentRevisionStatus**]({{complexTypePrefix}}CurrentRevisionStatus.md) | [**CurrentRevisionStatus**]({{complexTypePrefix}}CurrentRevisionStatus.md) |  | 

# MissionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Mission**]({{complexTypePrefix}}Mission.md) | [**Mission**]({{complexTypePrefix}}Mission.md) | [**Mission**]({{complexTypePrefix}}Mission.md) |  | 

# RemainInForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# RepealDateFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# RepealDateToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# RepealStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) | [**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) | [**RepealStatus**]({{complexTypePrefix}}RepealStatus.md) |  | 

# UpdatedFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# UpdatedToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

# ResponseFormatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResponseFormat]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) | [**ResponseFormat**]({{complexTypePrefix}}ResponseFormat.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
law_id_or_num | LawIdOrNumSchema | | 

# LawIdOrNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_revisions.ApiResponseFor200) | 200 リクエスト処理、レスポンス処理が正しく行えた時
400 | [ApiResponseFor400](#get_revisions.ApiResponseFor400) | 400 Bad Request API クライアント側の問題によるエラー発生時
500 | [ApiResponseFor500](#get_revisions.ApiResponseFor500) | 500 Internal Server Error サーバ内処理でエラー発生時

#### get_revisions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LawRevisionsResponse**](../../models/LawRevisionsResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**LawRevisionsResponse**](../../models/LawRevisionsResponse.md) |  | 


#### get_revisions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor400ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


#### get_revisions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


# SchemaFor500ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorInfo**](../../models/ErrorInfo.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

