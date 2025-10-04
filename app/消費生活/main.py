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
    ],
    "texts": []
  },
  {
    "law_title": "預託等取引に関する法律",
    "law_id": "361AC0000000062",
    "article_numbers": [
      [1], [2], 
      [9] # 勧誘等の禁止等
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
      [10] # 消費生活センターの設置等
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
    "law_title": "消費者の財産的被害等の集団的な回復のための民事の裁判手続の特例に関する法律",
    "law_id": "425AC0000000096",
    "article_numbers": [
      [1], [3]
    ],
    "texts": []
  },
  {
    "law_title": "特定デジタルプラットフォームの透明性及び公正性の向上に関する法律",
    "law_id": "502AC0000000038",
    "article_numbers": [
      [1], [2], [4]
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
