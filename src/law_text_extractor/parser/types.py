from typing import Callable, Dict, Any, Union, List

Node = Union[Dict[str, Any], str]
Context = List[Dict[str, Any]]

# ハンドラ関数は第4引数としてハンドラ辞書自身を受け取る
Handler = Callable[[Dict[str, Any], str, Context, 'Handlers'], str]
Handlers = Dict[str, Handler]
