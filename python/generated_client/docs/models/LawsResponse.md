# openapi_client.model.laws_response.LawsResponse

法令一覧取得API レスポンス

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 法令一覧取得API レスポンス | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | 返却するリスト（取得件数の上限（&#x60;limit&#x60;）、何件目から取得するか（&#x60;offset&#x60;）適用後）に含まれる項目数 | value must be a 64 bit integer
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | 取得件数の上限（&#x60;limit&#x60;）、何件目から取得するか（&#x60;offset&#x60;）適用前のリストに含まれる項目数（検索条件にマッチした全件数） | [optional] value must be a 64 bit integer
**next_offset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | 次の何件目から取得するか（&#x60;offset&#x60;）。末尾まで取得が完了した場合はnull | [optional] value must be a 64 bit integer
**[laws](#laws)** | list, tuple,  | tuple,  | 法令ID単位の法令情報 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# laws

法令ID単位の法令情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 法令ID単位の法令情報 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[law_info](#law_info)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 改正履歴に依存しない法令情報 | [optional] 
**[revision_info](#revision_info)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 取得した改正履歴における法令情報 | [optional] 
**[current_revision_info](#current_revision_info)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 最新の履歴における法令情報&lt;br&gt;法令の時点（&#x60;asof&#x60;）に依存しない現在以前の最新のリビジョン | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# law_info

改正履歴に依存しない法令情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 改正履歴に依存しない法令情報 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[LawInfo](LawInfo.md) | [**LawInfo**](LawInfo.md) | [**LawInfo**](LawInfo.md) |  | 

# revision_info

取得した改正履歴における法令情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 取得した改正履歴における法令情報 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RevisionInfo](RevisionInfo.md) | [**RevisionInfo**](RevisionInfo.md) | [**RevisionInfo**](RevisionInfo.md) |  | 

# current_revision_info

最新の履歴における法令情報<br>法令の時点（`asof`）に依存しない現在以前の最新のリビジョン

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 最新の履歴における法令情報&lt;br&gt;法令の時点（&#x60;asof&#x60;）に依存しない現在以前の最新のリビジョン | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RevisionInfo](RevisionInfo.md) | [**RevisionInfo**](RevisionInfo.md) | [**RevisionInfo**](RevisionInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

