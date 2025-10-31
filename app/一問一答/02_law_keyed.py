import os
import re
import json
from law_text_extractor.core.extractor import extract_law_texts_by_elm

def get_law_texts(law_id, elm):
    splitted = elm.split("-")
    article_elm = '-'.join(splitted[:2])
    result_text = extract_law_texts_by_elm(law_id, article_elm)
    if "error" in result_text:
        print(f'Error: {result_text["error"]}')
    else:
        if len(splitted) == 3 and splitted[-1].startswith("Paragraph"):
            texts = []
            if "第１項" not in result_text["texts"][0]:
                texts.append(result_text["texts"][0])
            result_text = extract_law_texts_by_elm(law_id, elm)
            if "error" in result_text:
                print(f'Error: {result_text["error"]}')
            else:
                texts.extend(result_text["texts"])
                return texts
        else:
            return result_text["texts"]
    return None

def extract_article_numbers(text):
    splitted_text = text.split("第")
    if 1 < len(splitted_text):
        art_str = text.split("第")[0]
        par_str = text.split("第")[-1]
    else:
        art_str = text
        par_str = None
    elm_str = f'MainProvision-Article_{"_".join([n for n in art_str.replace("民法","").replace("条","").split("の")])}'
    if par_str is not None:
        elm_str += f'-Paragraph_{par_str.replace("項","").replace("第","")}'
#    print(f'{text} : {elm_str}')
    return elm_str

def main():
    file_path_name = os.path.join(os.path.dirname(__file__),"一問一答_民法_law_added.json")
    print(os.path.isfile(file_path_name))
    with open(file_path_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    for sub_cat in data["sub_cats"]:
        sub_cat_all_laws = []
        print(sub_cat["title"])
        for q_and_a in sub_cat["q_and_a"]:
            sub_cat_all_laws.extend(q_and_a["laws"])

        sub_cat_all_laws = sorted(list(dict.fromkeys(sub_cat_all_laws)), key=lambda x: [int(n) for n in re.findall(r"\d+", x)])
        law_key_q_and_as = []
        for law in sub_cat_all_laws:
            print(law)
            law_texts = get_law_texts("129AC0000000089", extract_article_numbers(law))
            q_and_as = []
            for q_and_a in sub_cat["q_and_a"]:
                if law in q_and_a["laws"]:
                    q_and_as.append(q_and_a)
            law_key_q_and_as.append({
                "law": law,
                "law_texts": law_texts,
                "q_and_as": q_and_as
            })
        output_path_name = os.path.join(os.path.dirname(__file__),f'一問一答_民法_{sub_cat["title"]}_.json')
        with open(output_path_name, "w", encoding="utf-8") as f:
            json.dump(law_key_q_and_as, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
    pass