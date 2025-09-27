import re
import json
from law_text_extractor.api.client import get_law_id_by_title
from .law_reference import get_law_names, get_articlws_by_name


# 【Python3】括弧と括弧内文字列削除
# https://qiita.com/mynkit/items/d6714b659a9f595bcac8
def delete_brackets(s):
    """
    括弧と括弧内文字列を削除
    """
    """ brackets to zenkaku """
    table = {
        "(": "（",
        ")": "）",
        "<": "＜",
        ">": "＞",
        "{": "｛",
        "}": "｝",
        "[": "［",
        "]": "］"
    }
    for key in table.keys():
        s = s.replace(key, table[key])
    """ delete zenkaku_brackets """
    l = ['（[^（|^）]*）', '【[^【|^】]*】', '＜[^＜|^＞]*＞', '［[^［|^］]*］',
            '「[^「|^」]*」', '｛[^｛|^｝]*｝', '〔[^〔|^〕]*〕', '〈[^〈|^〉]*〉']
    for l_ in l:
        s = re.sub(l_, "", s)
    """ recursive processing """
    return delete_brackets(s) if sum([1 if re.search(l_, s) else 0 for l_ in l]) > 0 else s

def get_law_ids(law_names):
    result_obj = {}

    for law_name in law_names:
        # 関数を呼び出して法令IDを取得
        # 法令名の文字数が最も少ないものを採用
        print(law_name)
        found_laws = sorted(get_law_id_by_title(law_name), key=lambda x: len(x['law_title']))
        result_obj.update({law_name: found_laws[0] if 0 < len(found_laws) else {}})
    return result_obj    

def convert_to_article_numbers(name):
    articles = []
    for item in get_articlws_by_name(name):
        print(item)
        splitted = item.replace("条", "").split("第")
        articles.append([int(num_str, 10) for num_str in splitted[1].split("の") if re.match(r"^[1-9][0-9]*$", num_str)])
    result =  list(set(articles))
    return result

def main():
    for name in get_law_names():    
        result = convert_to_article_numbers(name)
    pass

def main2():
    law_name_obj = {}
    for name in get_law_names():
        law_name_obj.update({name: delete_brackets(name)})
    law_names = list(law_name_obj.values())
    law_ids = get_law_ids(law_names[:3])

    for name in law_name_obj:
        short_law_name = law_name_obj[name]
        if short_law_name in law_ids:
            law_ids[short_law_name].update({
                "law_id": law_ids[short_law_name].get("law_id", ""),
                "original_law_name": name,
                "reference_articles": convert_to_article_numbers(name)
            })

    print(json.dumps(law_ids, indent=2, ensure_ascii=False))
    pass

if __name__ == "__main__":
    main()

