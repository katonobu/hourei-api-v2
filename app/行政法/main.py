import os
from make_mp3.convert_to_mp3 import convert_to_mp3
from make_mp3.make_mp3 import MakeMp3

law_objs = [
    {
        "law_title": "行政手続法",
        "law_id": "405AC0000000088",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
            [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
            [21], [22], [23], [24], [25], [26], [27], [28], [29], [30],
            [31], [32], [33], [34], [35], 
            [36], [36,2], [36,3], 
            [37], [38], [39], [40],
            [41], [42], [43], [44], [45], [46]
        ],
        "texts": []
    },
    {
        "law_title": "行政不服審査法",
        "law_id": "426AC0000000068",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
            [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
            [21], [22], [23], [24], [25], [26], [27], [28], [29], [30],
            [31], [32], [33], [34], [35], [36], [37], [38], [39], [40],
            [41], [42], [43], [44], [45], [46], [47], [48], [49], [50],
            [51], [52], [53], [54], [55], [56], [57], [58], [59], [60],
            [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], 
            [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], 
            [81], [82], [83], [84], [85], [86], [87]
        ],
        "texts": []
    },
    {
        "law_title": "行政事件訴訟法",
        "law_id": "337AC0000000139",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
            [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], 
            [21], [22], [23], [23,2], [24], [25], [26], [27], [28], [29], [30], 
            [31], [32], [33], [34], [35], [36], 
            [37], [37,2], [37,3], [37,4], [37,5],
            [38], [39], [40],
            [41], [42], [43], [44], [45], [46], 
        ],
        "texts": []
    },
    {
        "law_title": "国家賠償法",
        "law_id": "322AC0000000125",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6]
        ],
        "texts": []
    },
]


def local_convert_to_mp3(base_dir, artist, album_name, target_objs, album_count=1, dry_run=False):
    mk_mp3 = MakeMp3()

    album_dir = os.path.join(base_dir, album_name)
    album_dir = os.path.join(base_dir, f'{album_count:02d}_{album_name}')

    os.makedirs(album_dir, exist_ok=True)

    album_title = f'{artist[:2]}…{album_count:02d} {album_name}'

    track_num = 1
    mk_mp3.init(dry_run=dry_run)
    mk_mp3.mp3_tts(
        os.path.join(album_dir, f'{track_num:02d}_{album_name}.mp3'),
        [album_name],
        track_num=track_num,
        title_str=f'{track_num:02d} {album_name}',
        artist_name_str=artist,
        album_name_str=album_title,
        rate=200
    )
    mk_mp3.finish()

    track_num += 1
    for item in target_objs:
        track_title = item["title"]
        mk_mp3.init(dry_run=dry_run)
        mk_mp3.mp3_tts(
            os.path.join(album_dir, f'{track_num:02d}_{album_name}.mp3'),
            ['\n'.join([track_title]+item["sentences"])],
            track_num=track_num,
            title_str=f'{track_num:02d} {track_title}',
            artist_name_str=artist,
            album_name_str=album_title,
            rate=280
        )
        mk_mp3.finish()
        track_num += 1
    return album_count + 1


def main():
    dry_run = True
    dry_run = False

    artist = "行政法"

    base_dir = os.path.join(os.path.dirname(__file__), "mp3_output", artist)
    os.makedirs(base_dir, exist_ok=True)

    album_count = 1
    album_count = convert_to_mp3(
        base_dir, artist, law_objs, album_count, dry_run=dry_run, normal_rate=280)

if __name__ == "__main__":
    main()
