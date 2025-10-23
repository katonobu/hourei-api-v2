import os
from make_mp3.convert_to_mp3 import convert_to_mp3

law_objs = [
  {
    "law_title": "民法",
    "law_id": "129AC0000000089",
    "article_numbers": [
      [1], [5], [6], 
      [95], [120], [121], [121, 2], 
      [521], [548, 2], [548, 4]            
    ],
    "texts": []
  },
  {
    "law_title": "家庭用品品質表示法",
    "law_id": "337AC0000000104",
    "article_numbers": [
      [1], [2]
    ],
    "texts": []
  },
  {
    "law_title": "不当景品類及び不当表示防止法",
    "law_id": "337AC0000000134",
    "article_numbers": [
      [1], [4], [5], [7]            
    ],
    "texts": []
  },
  {
    "law_title": "消費者基本法",
    "law_id": "343AC1000000078",
    "article_numbers": [
      [1], [2], [3], [4]
    ],
    "texts": []
  },
  {
    "law_title": "特定商取引に関する法律",
    "law_id": "351AC0000000057",
    "article_numbers": [
      [1], [2], 
      [3], [3,2], [4]
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
    "law_title": "電子消費者契約に関する民法の特例に関する法律",
    "law_id": "413AC0000000095",
    "article_numbers": [
      [1], [3]
    ],
    "texts": []
  },
  {
    "law_title": "消費者安全法",
    "law_id": "421AC0000000050",
    "article_numbers": [
      [1], [3], 
      [10], # 消費生活センターの設置等
      [10,3]
    ],
    "texts": []
  },
  {
    "law_title": "消費者契約法",
    "law_id": "412AC0000000061",
    "article_numbers": [
      [1], [2], [3], 
      [4], [7],  # 消費者契約の申込み又はその承諾の意思表示の取消し
      [8], [8,2], [8,3], [9], [10], # 消費者契約の条項の無効
      [12], [12,2] # 差止請求権等
    ],
    "texts": []
  },
  {
    "law_title": "デジタル社会形成基本法",
    "law_id": "503AC0000000035",
    "article_numbers": [
      # 総則
      [1], [2], 
      # 基本理念
      [3], [4],
      [5], [6], [7], [8],
      [9], [10], [11], [12],
      # 施策の策定に係る基本方針
      [20], [21], [22], [23],
      [24], [25], [26], [27],
      [28], [29], [30], [31],
      [32], [33], [34], [35],
      [36], [37], 
      # デジタル社会の形成に関する重点計画
      [39]
    ],
    "texts": []
  }
]

def main():
  dry_run = True
  dry_run = False

  artist = "消費生活"

  base_dir = os.path.join(os.path.dirname(__file__),"mp3_output", artist)
  os.makedirs(base_dir, exist_ok=True)

  convert_to_mp3(base_dir, artist, law_objs, album_count=1, dry_run=dry_run, normal_rate=280)

if __name__ == "__main__":
  main()
