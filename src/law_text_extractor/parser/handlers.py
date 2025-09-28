import json
from .types import Handler, Handlers, Context
from .recursive_parser import process_law_text_node_with_context, find_ancestor

def get_article_title(context: Context) -> str:
    """コンテキストから直近のArticleTitleのテキストを取得する。"""
    article_node = find_ancestor(context, 'Article')
    result_str = ""
    if not article_node:
        return result_str
    for child in article_node.get('children', []):
        if isinstance(child, dict) and child.get('tag') == 'ArticleTitle':
            for part in child.get('children', []):
                if isinstance(part, str):
                    result_str += part
                else:
                    print('Unexpected:ArticleTitle is supported only text')
    return result_str

def get_paragraph_title(context: Context) -> str:
    """コンテキストから直近のParagraphNumを取得する。"""
    para_node = find_ancestor(context, 'Paragraph')
    result_str = ""
    if not para_node:
        return result_str
    for child in para_node.get('children', []):
        if isinstance(child, dict) and child.get('tag') == 'ParagraphNum':
            for part in child.get('children', []):
                if isinstance(part, str):
                    result_str += part
                else:
                    print('Unexpected:ParagraphNum is supported only text')
    if 0 == len(result_str):
        result_str = "１"
    return result_str

def get_item_title(context: Context) -> str:
    """コンテキストから直近のItemTitleを取得する。"""
    item_node = find_ancestor(context, 'Item')
    result_str = ""
    if not item_node:
        return result_str
    for child in item_node.get('children', []):
        if isinstance(child, dict) and child.get('tag') == 'ItemTitle':
            for part in child.get('children', []):
                if isinstance(part, str):
                    result_str += part
                else:
                    print('Unexpected:ItemTitle is supported only text')
    return result_str

def get_subitem1_title(context: Context) -> str:
    """コンテキストから直近のItemTitleを取得する。"""
    item_node = find_ancestor(context, 'Subitem1')
    result_str = ""
    if not item_node:
        return result_str
    for child in item_node.get('children', []):
        if isinstance(child, dict) and child.get('tag') == 'Subitem1Title':
            for part in child.get('children', []):
                if isinstance(part, str):
                    result_str += part
                else:
                    print('Unexpected:Subitem1Title is supported only text')
    return result_str


# --- テキスト整形用ハンドラ関数群 ---

def _process_children(node, context, handlers):
    """子要素を再帰的に処理するためのヘルパー関数"""
    new_context = context + [node]
    return "".join(
        process_law_text_node_with_context(child, handlers, new_context)
        for child in node.get('children', [])
    )

def handle_text(text: str, context: Context, handlers: Handlers) -> str:
    return text

def handle_article_title(node, children_content, context, handlers):
    return _process_children(node, context, handlers)

def handle_article_caption(node, children_content, context, handlers):
    content = _process_children(node, context, handlers).strip()
    return content[1:-1] if content.startswith('（') and content.endswith('）') else content

def handle_paragraph(node, children_content, context, handlers):
    # spec4.md に基づき、ParagraphタグのNum属性を使用
    article_title = get_article_title(context)
    para_title = get_paragraph_title([node])
    sentence = _process_children(node, context, handlers).strip()
    return f"\n{article_title} 第{para_title}項 \n{sentence}"

def handle_item(node, children_content, context, handlers):
    para_title = get_paragraph_title(context)
    item_title = get_item_title([node])
    for c in node.get('children', []):
        if isinstance(c, dict) and c.get('tag') == 'ItemSentence':
            sentence = _process_children(node, context, handlers).replace(item_title, "").strip()
    return f"\n第{para_title}項 第{item_title}号 \n{sentence}"

def handle_paragraph_num(node, children_content, context, handlers):
    return "" # Paragraphのattr.Numを使うため、このタグのテキストは不要

def handle_ruby(node, children_content, context, handlers):
    base_text = ""
    ruby_text = ""
    for child in node.get('children', []):
        if isinstance(child, str):
            base_text += child
        if isinstance(child, dict) and child.get('tag') == 'Rt':
            for ruby_child in child.get('children', []):
                ruby_text += ruby_child
    # f'{漢字}({読み仮名})'の形式で返す場合
#    return f"{base_text}({ruby_text})"
    # 読み仮名を返す
    return f"{ruby_text}"

def handle_sup_sub(node, children_content, context, handlers):
    return _process_children(node, context, handlers)

def handle_line(node, children_content, context, handlers):
    return _process_children(node, context, handlers)

def handle_ignore(node, children_content, context, handlers):
    # spec4.md の通り、TableStruct, FigStructは処理対象外
    return ""

def handle_fixed_text(text: str):
    def handler(node, children_content, context, handlers):
        # spec4.md の通り、固定文字列を返す
        return text
    return handler

def handle_list(node, children_content, context, handlers):
    # spec4.md の通り、ListSentence直下のみ処理
    list_sentences = [child for child in node.get('children', []) if child.get('tag') == 'ListSentence']
    output = []
    for ls in list_sentences:
        output.append(_process_children(ls, context + [node], handlers))
    return " ".join(output)

def handle_article(node, children_content, context, handlers):
    """条全体の出力を組み立てるメインハンドラ"""
    article_title_text = ""
    caption_text = ""
    paragraph_texts = []

    for child in node.get('children', []):
        if not isinstance(child, dict): continue
        
        tag = child.get('tag')
        child_text = process_law_text_node_with_context(child, handlers, context + [node])

        if tag == 'ArticleTitle':
            article_title_text = child_text.strip()
        elif tag == 'ArticleCaption':
            caption_text = child_text.strip()
        elif tag == 'Paragraph':
            paragraph_texts += child_text.strip().split("\n")
            
    output_lines = []
    if caption_text:
        output_lines.append(f"{article_title_text} {caption_text}")
    output_lines += paragraph_texts
#    for para_text in paragraph_texts:
        # 各項のテキストを生成
#        parent_article = find_ancestor(context, 'Article')
        # Itemの処理でArticleTitleが重複しないように調整
#        if not para_text.startswith("第"): # Item, Subitemなどは項番号で始まらない
            # このロジックはより洗練させる余地あり
#            para_text = f"{article_title_text} {para_text}"
        
        # ParagraphからItemへArticleTitleを伝播させるため、Paragraphハンドラを修正
        # 今回は、元の要求(user_4)に近くするため、以下のように変更
        # 1. Paragraphは項番号と本文のみを返す
        # 2. Articleハンドラが、ArticleTitleを前置して組み立てる
#        para_full_text = f"{article_title_text} {para_text}"
        
        # Item,SubitemのハンドラでArticleTitle,ParagraphNumを参照できるようにcontextを渡す
        # paragraph_texts.append(child_text.strip())では不十分
        # ここではユーザーの要求に沿った出力形式(user_4)を優先する
#        output_lines.append(para_full_text)
        
    return "\n".join(output_lines)

# タグ名と処理関数をマッピングするハンドラ辞書
HANDLERS: Handlers = {
    '__text__': handle_text,
    'Article': handle_article,
    'ArticleTitle': handle_article_title,
    'ArticleCaption': handle_article_caption,
    'Paragraph': handle_paragraph,
    'ParagraphNum': handle_paragraph_num,
    'Item': handle_item,
    'Ruby': handle_ruby,
    'Sup': handle_sup_sub,
    'Sub': handle_sup_sub,
    'Line': handle_line,
    'TableStruct': handle_ignore,
    'FigStruct': handle_ignore,
    'List': handle_list,
    'QuoteStruct': handle_fixed_text("引用(略)"),
    'ArithFormula': handle_fixed_text("数式(略)"),
}
