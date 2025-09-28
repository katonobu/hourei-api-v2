import os
import re
import json
from law_text_extractor.core.extractor import extract_law_texts
from law_text_extractor.api.client import get_law_info
from make_mp3.make_mp3 import MakeMp3

def main():
    input_txt_path_name = os.path.join(os.path.dirname(__file__), "law_list.txt")

    article_id_objs = []
    with open(input_txt_path_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if 0 < len(line.strip()):
            url = line.strip().split("(")[-1].replace(")", "")
            [law_id, article_id] = url.split("/")[-1].split("#")
            for item in article_id.split("-"):
                if item.startswith("At_"):
                    article_numbers = [int(num, 10) for num in item.replace("At_", "").split("_")]
                    article_id_objs.append({
                        "law_id": law_id,
                        "article_numbers": article_numbers
                    })
#    print(json.dumps(article_id_objs, indent=2, ensure_ascii=False))
    law_ids = set([item["law_id"] for item in article_id_objs])

    id_to_title = {}
    law_obj = {}
    for law_id in law_ids:
        law_info = get_law_info(law_id)
        if law_info and "revision_info" in law_info and "law_title" in law_info["revision_info"]:
            law_title = law_info["revision_info"]["law_title"]
            law_obj.update({
                law_title:{
                    "law_title": law_title,
                    "law_id": law_id,
                    "article_numbers": [],
                    "texts":[]
                }
            })
            id_to_title.update({law_id:law_title})

    for item in article_id_objs:
        if "law_id" in item and item["law_id"] in id_to_title:
            title = id_to_title[item["law_id"]]
            law_obj[title]["article_numbers"].append(item["article_numbers"])
    law_objs = sorted([law_obj[key] for key in law_obj], key=lambda x: x["law_id"])

    mk_mp3 = MakeMp3()

    artist = "消費生活"
    base_dir = os.path.join(os.path.dirname(__file__),"mp3_output", artist)
    os.makedirs(base_dir, exist_ok=True)

    album_count = 1
    for law_obj in law_objs:
        print(f'法令: {law_obj["law_title"]} ({law_obj["law_id"]})')
        album_name = f'{album_count:02d} {law_obj["law_title"]}'
        album_dir = os.path.join(base_dir, album_name)
        os.makedirs(album_dir, exist_ok=True)
        for article_numbers in law_obj["article_numbers"]:
            print(f'  条文: 第{"の".join(map(str, article_numbers))}条')
            try:
                result = extract_law_texts(law_obj["law_id"], article_numbers)
            except Exception as e:
                result = {"error": str(e), "law_id": law_obj["law_id"], "article_numbers": article_numbers}
#            print(json.dumps(result, indent=2, ensure_ascii=False))
            if "texts" in result and 0 < len(result["texts"]):
                law_obj["texts"].append(result["texts"])
            else:
                law_obj["texts"].append(["エラー"])
        album_count += 1

    album_count = 1
    for law_obj in law_objs:
        album_name = f'{album_count:02d} {law_obj["law_title"]}'
        album_dir = os.path.join(base_dir, album_name)
        track_num = 1
        title_str = "law_name"
        mk_mp3.init(dry_run=False)
        mk_mp3.mp3_tts(
            os.path.join(album_dir, f'{track_num:02d}_law_name.mp3'), 
            [law_obj["law_title"]],
            track_num=track_num,
            title_str=title_str,
            artist_name_str=artist,
            album_name_str=album_name,
            rate=200
        )
        mk_mp3.finish()
        track_num += 1
        for texts, article_numbers in zip(law_obj["texts"], law_obj["article_numbers"]):
            title_str = f'AT_{"_".join(map(str, article_numbers))}'
            mk_mp3.init(dry_run=False)
            mk_mp3.mp3_tts(
                os.path.join(album_dir, f'{track_num:02d}_{title_str}.mp3'), 
                texts,
                track_num=track_num,
                title_str=title_str,
                artist_name_str=artist,
                album_name_str=album_name,
                rate=300
            )
            mk_mp3.finish()
            track_num += 1
        album_count += 1

if __name__ == "__main__":
    main()

