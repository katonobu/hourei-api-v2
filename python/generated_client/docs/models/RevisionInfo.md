# openapi_client.model.revision_info.RevisionInfo

法令の履歴に関する情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 法令の履歴に関する情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**law_revision_id** | str,  | str,  | 法令履歴ID | [optional] 
**[law_type](#law_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 法令種別 | [optional] 
**law_title** | str,  | str,  | 法令名 | [optional] 
**law_title_kana** | str,  | str,  | 法令名読み | [optional] 
**abbrev** | str,  | str,  | 法令略称 | [optional] 
**category** | str,  | str,  | 法令分野分類 | [optional] 
**updated** | str, datetime,  | str,  | 正誤等による更新日時 | [optional] value must conform to RFC-3339 date-time
**amendment_promulgate_date** | str, date,  | str,  | 改正法令公布日 | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**amendment_enforcement_date** | str, date,  | str,  | 改正法令施行期日（この履歴に対応する改正の施行期日） | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**amendment_enforcement_comment** | str,  | str,  | 施行期日規定等の参考情報（この履歴に対応する改正の施行期日） | [optional] 
**amendment_scheduled_enforcement_date** | str, date,  | str,  | 擬似的な施行期日（実際の施行期日とは限らない）（この履歴に対応する改正の施行期日） | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**amendment_law_id** | str,  | str,  | 改正法令の法令ID（この履歴に対応する改正法令） | [optional] 
**amendment_law_title** | str,  | str,  | 改正法令名 | [optional] 
**amendment_law_title_kana** | str,  | str,  | 改正法令名読み | [optional] 
**amendment_law_num** | str,  | str,  | 改正法令番号 | [optional] 
**[amendment_type](#amendment_type)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 改正種別 | [optional] 
**[repeal_status](#repeal_status)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 廃止等の状態 | [optional] 
**repeal_date** | None, str, date,  | NoneClass, str,  | 廃止日 | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**remain_in_force** | None, bool,  | NoneClass, BoolClass,  | 廃止後の効力（&#x60;true&#x60;:廃止後でも効力を有するもの / &#x60;false&#x60;:廃止後に効力を有しないもの） | [optional] 
**[mission](#mission)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 新規制定又は被改正法令（&#x60;New&#x60;）・一部改正法令（&#x60;Partial&#x60;） | [optional] 
**[current_revision_status](#current_revision_status)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 履歴の状態 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# law_type

法令種別

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 法令種別 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[LawType](LawType.md) | [**LawType**](LawType.md) | [**LawType**](LawType.md) |  | 

# amendment_type

改正種別

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 改正種別 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AmendmentType](AmendmentType.md) | [**AmendmentType**](AmendmentType.md) | [**AmendmentType**](AmendmentType.md) |  | 

# repeal_status

廃止等の状態

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 廃止等の状態 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RepealStatus](RepealStatus.md) | [**RepealStatus**](RepealStatus.md) | [**RepealStatus**](RepealStatus.md) |  | 

# mission

新規制定又は被改正法令（`New`）・一部改正法令（`Partial`）

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 新規制定又は被改正法令（&#x60;New&#x60;）・一部改正法令（&#x60;Partial&#x60;） | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Mission](Mission.md) | [**Mission**](Mission.md) | [**Mission**](Mission.md) |  | 

# current_revision_status

履歴の状態

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 履歴の状態 | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CurrentRevisionStatus](CurrentRevisionStatus.md) | [**CurrentRevisionStatus**](CurrentRevisionStatus.md) | [**CurrentRevisionStatus**](CurrentRevisionStatus.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

