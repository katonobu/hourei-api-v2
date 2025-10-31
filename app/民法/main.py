import os
import json
from law_text_extractor.api.client import get_law_data
from make_mp3.convert_to_mp3 import convert_to_mp3

law_objs = [
  {
    "law_title": "民法・総則",
    "law_id": "129AC0000000089",
    "elm": "MainProvision-Part_1",
    "article_numbers": [],
    "texts": []
  },
  {
    "law_title": "民法・物権",
    "law_id": "129AC0000000089",
    "elm": "MainProvision-Part_2",
    "article_numbers": [],
    "texts": []
  },
  {
    "law_title": "民法・債権",
    "law_id": "129AC0000000089",
    "elm": "MainProvision-Part_3",
    "article_numbers": [],
    "texts": []
  },
  {
    "law_title": "民法・親族",
    "law_id": "129AC0000000089",
    "elm": "MainProvision-Part_4",
    "article_numbers": [],
    "texts": []
  },
  {
    "law_title": "民法・相続",
    "law_id": "129AC0000000089",
    "elm": "MainProvision-Part_5",
    "article_numbers": [],
    "texts": []
  },
]

def recursive_call(obj, target_tag_handlers, output_obj):
#  print(f'{obj["tag"]}:{obj["attr"]["Num"]}')
  extract_children(obj, target_tag_handlers, output_obj),

def append_article_handler(obj, target_tag_handlers, output_obj):
  article_num_str = obj["attr"]["Num"]
  if ":" in article_num_str:
    article_num = None
  elif "_" in article_num_str:
    article_num = [int(n) for n in article_num_str.split("_")]
  else:
    article_num = [int(article_num_str)]
#  print(f'Article:{article_num}')
  if article_num is not None:
    output_obj["at_nums"].append(article_num)

def extract_children(obj, target_tag_handlers, output_obj):
  if "children" in obj:
    for child in obj["children"]:
      if "tag" in child and child["tag"] in target_tag_handlers:
        handler = target_tag_handlers[child["tag"]]
        handler(child, target_tag_handlers, output_obj)

def main():
  dry_run = True
  dry_run = False

#  artist = "民法 1_4倍速"
  artist = "民法"

  base_dir = os.path.join(os.path.dirname(__file__),"mp3_output", artist)
  os.makedirs(base_dir, exist_ok=True)

  for album_count, law_obj in enumerate(law_objs, start=1):
    got_obj = get_law_data(law_obj["law_id"],law_obj["elm"])
#    print(json.dumps(part_obj, ensure_ascii=False, indent=2))
#    with open(os.path.join(base_dir, "part_1_law_texts.json"), "w", encoding="utf-8") as f:
#      json.dump(got_obj, f, ensure_ascii=False, indent=2)

    handlers = {
      "Chapter": recursive_call,
      "Section": recursive_call,
      "Article": append_article_handler
    }

    if "law_full_text" in got_obj:
      output_obj = {"at_nums":[]}
      extract_children(
        got_obj["law_full_text"],
        handlers,
        output_obj
      )
      law_obj["article_numbers"] = output_obj["at_nums"]
#      print(json.dumps(law_obj, ensure_ascii=False, indent=2))

#      convert_to_mp3(base_dir, artist, [law_obj], album_count=album_count, dry_run=dry_run, normal_rate=280)
      convert_to_mp3(base_dir, artist, [law_obj], album_count=album_count, dry_run=dry_run, normal_rate=200)


if __name__ == "__main__":
  main()
