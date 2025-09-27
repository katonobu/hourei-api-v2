# hourei-api-v2
法令API Ver2 向け

## 法令テキスト抽出ツール (Law Text Extractor)

e-Gov法令API Version 2を利用して、指定された法令の条文を抽出し、指定のフォーマットでテキスト化するツールです。

### セットアップ

```bash
pip install -r requirements.txt
```

### 使い方

```bash
# 民法第三十条のテキストを取得
python src/law_text_extractor/main.py --law-id "129AC0000000089" --article-num "30"
```
