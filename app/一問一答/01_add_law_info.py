import os
import re
import json

def main():
    file_path_name = os.path.join(os.path.dirname(__file__),"一問一答_民法.json")
    print(os.path.isfile(file_path_name))
    with open(file_path_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    for sub_cat in data["sub_cats"]:
        print(sub_cat["title"])
        for q_and_a in sub_cat["q_and_a"]:
            text = q_and_a["exp"]
            matches = []
            for m in re.findall(r"民法\d+条(?:の\d+)?(?:第?\d+項)?", text):
                if "項" in m and "第" not in m:
                    m = re.sub(r"(\d+)項", r"第\1項", m)
                matches.append(m)
            extra_pattern = r"(民法\d+条(?:の\d+)?)(?:、(\d+)項)"
            for base, extra in re.findall(extra_pattern, text):
                m = f"{base}第{extra}項"
                matches.append(m)
            matches = list(dict.fromkeys(matches))                
            q_and_a["laws"] = matches

    output_path_name = os.path.join(os.path.dirname(__file__),f'一問一答_民法_law_added_.json')
    with open(output_path_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
    pass