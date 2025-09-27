import json
from law_text_extractor.core.extractor import extract_law_texts

def main():
    # spec4.mdの機能概要を実装したコアモジュールを呼び出す
    result = extract_law_texts("129AC0000000089", [30])
    
    # 結果をJSON形式で標準出力に出力
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
