# openapi_client.model.keyword_response.KeywordResponse

キーワード検索APIレスポンス

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | キーワード検索APIレスポンス | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | 指定&#x60;keyword&#x60;でヒットした総件数 | [optional] value must be a 64 bit integer
**sentence_count** | decimal.Decimal, int,  | decimal.Decimal,  | レスポンス単位で表示した&#x60;sentences&#x60;数の総和 | [optional] value must be a 64 bit integer
**next_offset** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | 次指定する&#x60;offset&#x60;値。末尾まで取得が完了した場合はnull | [optional] value must be a 64 bit integer
**[items](#items)** | list, tuple,  | tuple,  | 法令ID単位の情報リスト&lt;br&gt; * &#x60;revision_info&#x60; - 指定時点において効力を持つ版のメタ情報  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

法令ID単位の情報リスト<br> * `revision_info` - 指定時点において効力を持つ版のメタ情報 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 法令ID単位の情報リスト&lt;br&gt; * &#x60;revision_info&#x60; - 指定時点において効力を持つ版のメタ情報  | 

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
**law_info** | [**LawInfo**](LawInfo.md) | [**LawInfo**](LawInfo.md) |  | [optional] 
**revision_info** | [**RevisionInfo**](RevisionInfo.md) | [**RevisionInfo**](RevisionInfo.md) |  | [optional] 
**[sentences](#sentences)** | list, tuple,  | tuple,  | 検索ヒット箇所一覧 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sentences

検索ヒット箇所一覧

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | 検索ヒット箇所一覧 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | 添付ファイル情報 | 

# items

添付ファイル情報

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | 添付ファイル情報 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[position](#position)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 検索ヒットの場所 | [optional] 
**text** | str,  | str,  | 条文内容です。ハイライト箇所は&#x60;&lt;span&gt;&#x60;タグで囲まれます。XMLでのレスポンスの場合、タグはエスケープされることにご注意ください。 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# position

検索ヒットの場所

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 検索ヒットの場所 | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

