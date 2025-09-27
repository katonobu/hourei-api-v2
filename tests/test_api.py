import pytest
from unittest.mock import Mock

# テスト対象のモジュールと例外クラスをインポート
from law_text_extractor.api import client
from law_text_extractor.api.exceptions import APIRequestError

# --- テスト用の定数 ---
TEST_LAW_ID = "129AC0000000089"
TEST_ELM = "MainProvision-Article_30"
EXPECTED_URL = f"https://laws.e-gov.go.jp/api/2/law_data/{TEST_LAW_ID}"


def test_get_law_data_success(mocker):
    """
    正常系テスト: APIがステータスコード200で成功レスポンスを返した場合のテスト。
    """
    # 1. 準備 (Arrange)
    # 成功時のAPIレスポンスのダミーデータを作成
    mock_success_response = {
        "law_info": {"law_id": TEST_LAW_ID},
        "law_full_text": {"tag": "Article", "attr": {"Num": "30"}, "children": []}
    }
    
    # requests.get の戻り値となるモックオブジェクトを作成
    mock_response = Mock()
    mock_response.status_code = 200
    # .json() メソッドを呼び出すと mock_success_response を返すように設定
    mock_response.json.return_value = mock_success_response
    
    # mocker を使って、実際に requests.get が呼ばれたら上記のモックを返すように設定
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # 2. 実行 (Act)
    # テスト対象の関数を呼び出す
    result = client.get_law_data(TEST_LAW_ID, TEST_ELM)
    
    # 3. 検証 (Assert)
    # 返り値が期待通りか検証
    assert result == mock_success_response
    
    # requests.get が期待したURLとパラメータで1回だけ呼び出されたか検証
    mock_get.assert_called_once_with(
        EXPECTED_URL,
        params={
            "elm": TEST_ELM,
            "response_format": "json"
        }
    )

def test_get_law_data_raises_api_error_on_400(mocker):
    """
    異常系テスト: APIがステータスコード400 (Bad Request) を返した場合のテスト。
    """
    # 1. 準備 (Arrange)
    # 400エラー時のAPIレスポンスのダミーデータを作成 (V2仕様書参考 [2, 8])
    mock_error_response = {
        "code": "400004",
        "message": "日付（asof等）が誤っています。"
    }
    
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.headers = {'Content-Type': 'application/json'}
    mock_response.json.return_value = mock_error_response

    mocker.patch('requests.get', return_value=mock_response)
    
    # 2. 実行 & 3. 検証 (Act & Assert)
    # APIRequestError が送出されることを pytest.raises で検証
    with pytest.raises(APIRequestError) as excinfo:
        client.get_law_data(TEST_LAW_ID, TEST_ELM)
    
    # 送出された例外のメッセージが期待通りか検証
    assert mock_error_response["message"] in str(excinfo.value)

def test_get_law_data_raises_api_error_on_500(mocker):
    """
    異常系テスト: APIがステータスコード500 (Internal Server Error) を返した場合のテスト。
    """
    # 1. 準備 (Arrange)
    # 500エラー時のAPIレスポンスのダミーデータを作成 (V2仕様書参考 [3, 9])
    mock_error_response = {
        "code": "500001",
        "message": "サーバ内処理で異常が発生しました。"
    }

    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.headers = {'Content-Type': 'application/json'}
    mock_response.json.return_value = mock_error_response

    mocker.patch('requests.get', return_value=mock_response)

    # 2. 実行 & 3. 検証 (Act & Assert)
    with pytest.raises(APIRequestError) as excinfo:
        client.get_law_data(TEST_LAW_ID, TEST_ELM)

    # 送出された例外のメッセージが期待通りか検証
    assert mock_error_response["message"] in str(excinfo.value)