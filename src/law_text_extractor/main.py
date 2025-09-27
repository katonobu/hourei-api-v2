import argparse
import json
from .core.extractor import extract_law_texts

def main():
    """
    コマンドラインからの入力を受け付け、法令テキスト抽出処理を実行するエントリーポイント。
    """
    parser = argparse.ArgumentParser(description="e-Gov法令APIから条文テキストを抽出します。")
    parser.add_argument("--law-id", required=True, help="法令ID (例: 129AC0000000089)")
    parser.add_argument("--article-num", required=True, help="条文番号 (例: 30, 30_2)")
    
    args = parser.parse_args()
    
    # 条文番号文字列を数値のリストに変換
    try:
        article_nums = [int(n) for n in args.article_num.split('_')]
    except ValueError:
        print("エラー: --article-num は数値またはアンダースコア区切りの数値を指定してください。")
        return

    # spec4.mdの機能概要を実装したコアモジュールを呼び出す
    result = extract_law_texts(args.law_id, article_nums)
    
    # 結果をJSON形式で標準出力に出力
    print(json.dumps(result, indent=2, ensure_ascii=False))

def main2():
    # spec4.mdの機能概要を実装したコアモジュールを呼び出す
    result = extract_law_texts("129AC0000000089", [30])
    
    # 結果をJSON形式で標準出力に出力
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main2()
