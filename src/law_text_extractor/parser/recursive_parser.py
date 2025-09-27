from .types import Node, Context, Handlers
from typing import Dict, Union

def process_law_text_node_with_context(
    node: Node, 
    handlers: Handlers, 
    context: Context = None
) -> str:
    """
    コンテキストとハンドラ辞書を引き回しながら再帰的にJSONをパースする。
    """
    if context is None:
        context = []
    
    if isinstance(node, str):
        handler = handlers.get('__text__', lambda text, ctx, h: text)
        return handler(node, context, handlers)

    if not isinstance(node, dict) or 'tag' not in node:
        return ""

    new_context = context + [node]
    
    # 子要素を先に処理するのではなく、ハンドラが必要に応じて処理を制御する
    tag = node.get('tag')
    handler = handlers.get(tag)

    if handler:
        # ハンドラが存在すれば、処理を委譲
        # 子要素の処理はハンドラ内部で行う
        return handler(node, "", context, handlers) # children_contentは空で渡す
    else:
        # ハンドラがなければ、子要素をデフォルトで連結する
        return "".join(
            process_law_text_node_with_context(child, handlers, new_context)
            for child in node.get('children', [])
        )

def find_ancestor(context: Context, tag_name: str) -> Union[Dict, None]:
    """コンテキストから直近の祖先ノードを探す。"""
    for node in reversed(context):
        if node.get('tag') == tag_name:
            return node
    return None
