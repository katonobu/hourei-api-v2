import os
import json
from make_mp3.make_mp3 import MakeMp3

def local_convert_to_mp3(base_dir, artist, album_name, target_objs, album_count=1, dry_run=False):
    mk_mp3 = MakeMp3()

    album_dir = os.path.join(base_dir, album_name)
    album_dir = os.path.join(base_dir, f'{album_count:02d}_{album_name}')

    os.makedirs(album_dir, exist_ok=True)

    album_title = f'{artist[:2]}…{album_count:02d} {album_name}'

    track_num = 1
    for item in target_objs:
        print(item["title"])
        track_title = item["title"]
        mk_mp3.init(dry_run=dry_run)
        mk_mp3.mp3_tts(
            os.path.join(album_dir, f'{track_num:02d}_{album_name}.mp3'),
            ['\n'.join(item.get("sentences",[]))],
            track_num=track_num,
            title_str=f'{track_num:03d} {track_title}',
            artist_name_str=artist,
            album_name_str=album_title,
            rate=item.get("rate",280),
            additional_texts_objs=item.get("additional_texts_objs", None)
        )
        mk_mp3.finish()
        track_num += 1
    return album_count + 1


def main():
    dry_run = True
    dry_run = False

    mute_msec = 500
    rate = 240

    artist = "法文付 一問一答 民法"

    base_dir = os.path.join(os.path.dirname(__file__),"mp3_output", artist)
    os.makedirs(base_dir, exist_ok=True)


    file_path_name = os.path.join(os.path.dirname(__file__),"一問一答_民法_law_added.json")
    print(os.path.isfile(file_path_name))
    with open(file_path_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    sub_cats = [sc["title"] for sc in data["sub_cats"]]

    album_count = 1
    for sub_cat in sub_cats:
        print(sub_cat)
        input_path_name = os.path.join(os.path.dirname(__file__),f'一問一答_民法_{sub_cat}.json')
        with open(input_path_name, "r", encoding="utf-8") as f:
            law_key_q_and_as = json.load(f)

        target_objs = []
        for law_obj in law_key_q_and_as:
#            print(law_obj["law"])
            sentences = [law_obj["law"]]
            sentences += law_obj["law_texts"]
            target_objs.append({
                "title":law_obj["law"],
                "sentences":sentences,
                "rate":rate
            })
            for idx, q_and_a in enumerate(law_obj["q_and_as"], start = 1):
                title = f'{law_obj["law"]} 問題 {idx}'
                sentences = [title, q_and_a["question"]]
                ato = {"texts":[q_and_a["seigo"]],"mute_msec":mute_msec}
                target_objs.append({
                    "title":title,
                    "sentences":sentences,
                    "additional_texts_objs":[ato],
                    "rate":rate
                })

        album_count = local_convert_to_mp3(base_dir, artist, sub_cat, target_objs, album_count, dry_run)
  

if __name__ == "__main__":
    main()
