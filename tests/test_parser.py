# tests/test_parser.py

import json
import pathlib

# テスト対象のパーサー関数とハンドラ辞書をインポート
from law_text_extractor.parser.recursive_parser import process_law_text_node_with_context
from law_text_extractor.parser.handlers import HANDLERS

# テストデータが格納されているディレクトリへのパスを取得
TEST_DATA_DIR = pathlib.Path(__file__).parent / "data"


def test_parser_processes_minpo_30_correctly():
    """
    正常系テスト: 民法第三十条のJSONデータを正しくテキストに変換できるか検証する。
    """
    # 1. 準備 (Arrange)
    # テスト用のJSONファイルを読み込む
    json_path = TEST_DATA_DIR / "minpo_30.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        # このJSONデータは、APIから取得される law_full_text の部分に相当する
        law_full_text_data = json.load(f)

    # spec4.mdの仕様と、その後の対話で決定した期待される出力テキストを定義
    expected_output = """
    第三十条 失そうの宣告
    第三十条 第1項 不在者の生死が七年間明らかでないときは、家庭裁判所は、利害関係人の請求により、失そうの宣告をすることができる。
    第三十条 第2項 戦地に臨んだ者、沈没した船舶の中に在った者その他死亡の原因となるべき危難に遭遇した者の生死が、それぞれ、戦争がやんだ後、船舶が沈没した後又はその他の危難が去った後一年間明らかでないときも、前項と同様とする。
    """

    # 2. 実行 (Act)
    # テスト対象のパーサー関数を、テストデータとハンドラ辞書で実行
    actual_output = process_law_text_node_with_context(
        law_full_text_data,
        HANDLERS
    )

    # 3. 検証 (Assert)
    # 比較しやすいように、期待値と実際の出力の前後の空白を除去し、行ごとに分割してリスト化する
    expected_lines = [line.strip() for line in expected_output.strip().split('\n')]
    actual_lines = [line.strip() for line in actual_output.strip().split('\n')]
    
    # リストの内容が完全に一致することを検証
    assert actual_lines == expected_lines

