import pdfplumber
import re
import os

_PDF_PATH = "1407073_11_1_2.pdf"
PDF_PATH = os.path.join(os.path.dirname(__file__), _PDF_PATH)
_OUTPUT_PATH = "info_I_pages30_48.txt"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), _OUTPUT_PATH)

START_PAGE = 30  # PDFのページ番号（1始まり）
END_PAGE   = 48  # PDFのページ番号（1始まり）

# 情報Ⅱに入ったら止めるための判定用
STOP_PATTERN = re.compile(r"第２節\s*情報Ⅱ")

lines = []

with pdfplumber.open(PDF_PATH) as pdf:
    for page_index in range(START_PAGE - 1, END_PAGE):
        page = pdf.pages[page_index]

        text = page.extract_text()
        if not text:
            continue

        # 行単位で処理（欠落防止）
        for line in text.splitlines():
            # 情報Ⅱが出たら終了
            if STOP_PATTERN.search(line):
                break
            lines.append(line)

# UTF-8で保存
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"抽出完了: {OUTPUT_PATH}")
print(f"行数: {len(lines)}")