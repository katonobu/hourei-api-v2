import requests
from .exceptions import APIRequestError

# 法令一覧取得APIのエンドポイントURL
# ソース,より、Version 2のベースURLとパスを指定
BASE_URL = "https://laws.e-gov.go.jp/api/2" #

def get_law_id_by_title(law_title: str):
    """
    e-Gov法令API Version 2 を使用して、法令名から法令IDを取得します。
    APIは部分一致検索を行うため、複数の結果が返される可能性があります。

    Args:
        law_title (str): 検索したい法令名（部分一致可）

    Returns:
        list[dict]: 法令名と法令IDのペアを含む辞書のリスト。
                    見つからない場合やエラー時は空のリストを返します。
    """
    # APIに渡すパラメータ
    # law_title: 法令名（部分一致）
    # response_format: レスポンス形式をJSONに指定
    endpoint = f"{BASE_URL}/laws"
    params = {
        "law_title": law_title,
        "response_format": "json"
    }

    results = []
    try:
        # HTTP GETリクエストを送信
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # 200番台以外のステータスコードの場合、例外を発生させる

        # レスポンスをJSONとしてパース
        data = response.json()

        # 'laws'キーに法令情報のリストが含まれている
        if "laws" in data and data["laws"]:
            for law in data["laws"]:
                # 各法令情報から法令IDと法令名を取得
                # 法令IDは'law_info'内に
                # 法令名は'revision_info'内に
                law_id = law.get("law_info", {}).get("law_id")
                law_name = law.get("revision_info", {}).get("law_title")
                
                if law_id and law_name:
                    results.append({"law_title": law_name, "law_id": law_id})
        else:
            print(f"「{law_title}」に一致する法令は見つかりませんでした。")

    except requests.exceptions.RequestException as e:
        print(f"APIリクエスト中にエラーが発生しました: {e}")
        # エラーレスポンスの内容を表示
        if 'response' in locals() and response.text:
            print(f"エラーレスポンス: {response.text}")

    return results

def get_law_info(law_id: str):
    """
    e-Gov法令API Version 2 を使用して、法令IDから法令情報を取得します。
    APIは部分一致検索を行うため、複数の結果が返される可能性があります。
    Args:
        law_id (str): 取得したい法令の法令ID

    Returns:
        dict: 法令IDに対応する法令情報
              見つからない場合やエラー時は空のリストを返します。
    """
    # APIに渡すパラメータ
    # law_id: 法令id
    # response_format: レスポンス形式をJSONに指定
    endpoint = f"{BASE_URL}/laws"
    params = {
        "law_id": law_id,
        "response_format": "json"
    }

    result = {}
    try:
        # HTTP GETリクエストを送信
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # 200番台以外のステータスコードの場合、例外を発生させる

        # レスポンスをJSONとしてパース
        data = response.json()

        # 'laws'キーに法令情報のリストが含まれている
        if "laws" in data and data["laws"] and 0 < len(data["laws"]) and "law_info" in data["laws"][0]:
            result = data["laws"][0]
        else:
            return {}

    except requests.exceptions.RequestException as e:
        print(f"APIリクエスト中にエラーが発生しました: {e}")
        # エラーレスポンスの内容を表示
        if 'response' in locals() and response.text:
            print(f"エラーレスポンス: {response.text}")

    return result

def get_law_data(law_id: str, elm: str) -> dict:
    """
    法令本文取得API(/law_data)を呼び出し、法令本文のJSONデータを取得する。
    """
    endpoint = f"{BASE_URL}/law_data/{law_id}"
    params = {
        "elm": elm,
        "response_format": "json" #
    }
    
    response = requests.get(endpoint, params=params)
    
    # spec4.md のエラーハンドリング仕様
    if response.status_code != 200:
        error_info = response.json() if response.headers.get('Content-Type') == 'application/json' else {}
        message = error_info.get('message', f"HTTP Status Code: {response.status_code}")
        raise APIRequestError(message)
    
    return response.json()
