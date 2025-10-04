import os
from law_text_extractor.core.extractor import extract_law_texts
from make_mp3.make_mp3 import MakeMp3

"""
ToDo
- fetch処理は外に出したい。
- law_objsの構成変更、"texts","title"をキーとするオブジェクトとし、APIから取得するための情報と音声変換入力を分離する
"""

def convert_to_mp3(base_dir, artist, law_objs, album_count=1, dry_run=False, slow_rate=200, normal_rate=300):
    mk_mp3 = MakeMp3()
    for law_obj in law_objs:
        print(f'fetching {law_obj["law_title"]}...')
        for article_numbers in law_obj["article_numbers"]:
            try:
                result = extract_law_texts(law_obj["law_id"], article_numbers)
            except Exception as e:
                result = {"error": str(e), "law_id": law_obj["law_id"], "article_numbers": article_numbers}
            if "texts" in result and 0 < len(result["texts"]):
                law_obj["texts"].append(result["texts"])
            else:
                law_obj["texts"].append(["エラー"])

    for law_obj in law_objs:
        album_name = f'{artist[:2]}…{album_count:02d} {law_obj["law_title"]}'
        album_dir = os.path.join(base_dir, album_name)
        track_num = 1
        mk_mp3.init(dry_run=dry_run)
        mk_mp3.mp3_tts(
            os.path.join(album_dir, f'{track_num:02d}_law_name.mp3'), 
            [law_obj["law_title"]],
            track_num=track_num,
            title_str=law_obj["law_title"],
            artist_name_str=artist,
            album_name_str=album_name,
            rate=slow_rate
        )
        mk_mp3.finish()
        track_num += 1
        for texts, article_numbers in zip(law_obj["texts"], law_obj["article_numbers"]):
            title_str = f'AT_{"_".join(map(str, article_numbers))}'
            mk_mp3.init(dry_run=dry_run)
            mk_mp3.mp3_tts(
                os.path.join(album_dir, f'{track_num:02d}_{title_str}.mp3'), 
                texts,
                track_num=track_num,
                title_str=title_str,
                artist_name_str=artist,
                album_name_str=album_name,
                rate=normal_rate
            )
            mk_mp3.finish()
            track_num += 1
        album_count += 1
    return album_count
