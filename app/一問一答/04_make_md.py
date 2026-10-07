import os
import json
from make_mp3.make_mp3 import MakeMp3

def main():
    dry_run = True
    dry_run = False

    mute_msec = 500
    rate = 240

    artist = "法文付 一問一答 民法"

    base_dir = os.path.join(os.path.dirname(__file__),"md_output", artist)
    os.makedirs(base_dir, exist_ok=True)


    file_path_name = os.path.join(os.path.dirname(__file__),"一問一答_民法_law_added.json")
    print(os.path.isfile(file_path_name))
    with open(file_path_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    sub_cats = [sc["title"] for sc in data["sub_cats"]]

    for sub_cat in sub_cats:
        print(sub_cat)
        output_path_name = os.path.join(os.path.dirname(__file__),f'一問一答_民法_{sub_cat}.json')
        with open(output_path_name, "r", encoding="utf-8") as f:
            law_key_q_and_as = json.load(f)

        output_strs = []
        for law_obj in law_key_q_and_as:
            output_strs.append(f'# {law_obj["law"]}')
            output_strs.append(f'## {law_obj["law"]} 条文')
            indent = 0
            for text in law_obj["law_texts"]:
                additional_indent = 0
                splitted = text.strip().split()
                if splitted[-1].startswith("第") and splitted[-1].endswith("号"):
                    indent = 4
                elif splitted[-1].startswith("第") and splitted[-1].endswith("項"):
                    indent = 2
                elif splitted[0].startswith("第") and splitted[0].endswith("条"):
                    indent = 0
                else:
                    additional_indent = 2
                head_space = " "*(indent + additional_indent)
                output_strs.append(f'{head_space}- {text}')
            for idx, q_and_a in enumerate(law_obj["q_and_as"], start = 1):
                output_strs.append(f'## {law_obj["law"]} 問題 {idx}')
                output_strs.append(f'{q_and_a["question"]}')
                output_strs.append(f'## {law_obj["law"]} 解説 {idx}')
                output_strs.extend(q_and_a["exp"].split("\n"))


        output_path_name = os.path.join(base_dir,f'一問一答_民法_{sub_cat}.md')
        with open(output_path_name, "w", encoding="utf-8") as f:
            f.write("\n".join(output_strs))

if __name__ == "__main__":
    main()
