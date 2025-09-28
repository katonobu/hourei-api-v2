import os
from make_mp3.convert_to_mp3 import convert_to_mp3

law_objs = [
  {
    "law_title": "技術士法",
    "law_id": "358AC0000000025",
    "article_numbers": [
      [1],[2],[3],
      [44],[45],[45,2],[46],[47],[47,2]
    ],
    "texts": []
  },
  {
    "law_title": "製造物責任法",
    "law_id": "406AC0000000085",
    "article_numbers": [
      [1],[2],[3],[4],[5]
    ],
    "texts": []
  },
  {
    "law_title": "不正競争防止法",
    "law_id": "405AC0000000047",
    "article_numbers": [
      [1],[2]
    ],
    "texts": []
  },
  {
    "law_title": "個人情報の保護に関する法律",
    "law_id": "415AC0000000057",
    "article_numbers": [
      [1]
    ],
    "texts": []
  },
]

def main():
  dry_run = True
  dry_run = False

  artist = "技術士"

  base_dir = os.path.join(os.path.dirname(__file__),"mp3_output", artist)
  os.makedirs(base_dir, exist_ok=True)

  convert_to_mp3(base_dir, artist, law_objs, album_count=1, dry_run=dry_run)

if __name__ == "__main__":
  main()
