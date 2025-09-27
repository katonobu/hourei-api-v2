from typing import List, Dict, Any
from ..api import client
from ..api.exceptions import APIRequestError
from ..parser import recursive_parser
from ..parser import handlers as text_handlers

def extract_law_texts(law_id: str, article_nums: List[int]) -> Dict[str, Any]:
    """
    spec4.mdで定義された一連の処理を実行する。
    1. APIクライアントを呼び出して法令本文データを取得する。
    2. パーサーとハンドラを使ってJSONをテキストに変換する。
    3. 最終的な出力オブジェクトを返す。
    """
    # spec4.md の内部処理仕様に基づき、elmパラメータを生成
    elm_param = f"MainProvision-Article_{'_'.join(map(str, article_nums))}"
    
    try:
        # 法令本文取得APIを呼び出し
        law_data = client.get_law_data(law_id, elm_param)
        law_full_text = law_data.get("law_full_text")

        if not law_full_text:
            return {"texts": [], "error": "指定された条文の本文が見つかりません。"}

        # パーサーを実行し、テキストを生成
        result_text = recursive_parser.process_law_text_node_with_context(
            law_full_text, 
            text_handlers.HANDLERS
        )
        
        # 出力仕様に合わせて整形
        texts = [line for line in result_text.strip().split('\n') if line]
        return {"texts": texts}

    except APIRequestError as e:
        # spec4.md のエラーハンドリング仕様
        return {"texts": [], "error": str(e)}
