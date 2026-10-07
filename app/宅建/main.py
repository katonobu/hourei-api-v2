import os
from make_mp3.convert_to_mp3 import convert_to_mp3
from make_mp3.make_mp3 import MakeMp3

law_objs = [
    {
        "law_title": "宅地建物取引業法",
        "law_id": "327AC1000000176",
        "article_numbers": [
            [1], [2], 

            [3], [3,2], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], 
            
            [15], [15,2], [15,3], [16], [17], [18], [19], [19,2], [20],
            [21], [22], [22,2], [22,3], [22,4], [24], 
            
            [25], [26], [27], [28], [29], [30],

            [31], [31,2], [31,3], [32], [33], [33,2], [34], [34,2], [34,3], [35], [35,2], [36], [37], [37,2], [38], [39], [40],
            [41], [41,2], [42], [43], [44], [45], [46], [47], [47,2], [47,3], [48], [49], [50], [50,2],[50,2,2], [50,2,3],[50,2,4],
            [50,2,5], [50,3], [50,4], [50,5], [50,6], [50,7], [50,8], [50,9], [50,10], [50,11], [50,12],[50,13], [50,14], [50,15],
            [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], [61], [62], [63], [63,2], 
            [63,3], [63,4], [63,5], [64], 
            [64,2], [64,3], [64,4], [64,5], [64,6], [64,7], [64,8], [64,9], 
            [64,10], [64,11], [64,12], [64,13], [64,14], [64,15], [64,16], [64,17], [64,17,2], [64,18], [64,19],
            [64,20], [64,21], [64,22], [64,23], [64,24], [64,25],

            [65], [66], [67], [67,2], [68], [68,2], [69], [70], 
            [71], [71,2], [72], [78]
        ],
        "texts": []
    },
    {
        "law_title": "借地借家法",
        "law_id": "403AC0000000090",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
            [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
            [21], [22], [23], [24], [25], [26], [27], [28], [29], [30],
            [31], [32], [33], [34], [35], [36], [37], [38], [39], [40],
            [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], 
            [51], [52], [53], [54], [55], [56], [57], [58], [59], [60],
            [61]
        ],
        "texts": []
    },
    {
        "law_title": "建物の区分所有等に関する法律",
        "law_id": "337AC0000000069",
        "article_numbers": [
            [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
            [11], [12], [13], [14], [15], [16], [17], [18], [19], [20],
            [21], [22], [23], [24], [25], [26], [27], [28], [29], [30],
            [31], [32], [33], [34], [35], [36], [37], [38], [39], [40],
            [41], [42], [43], [44], [45], [46]
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

    artist = "宅建"

    base_dir = os.path.join(os.path.dirname(__file__), "mp3_output", artist)
    os.makedirs(base_dir, exist_ok=True)

    album_count = 1
    album_count = convert_to_mp3(
        base_dir, artist, law_objs, album_count, dry_run=dry_run, normal_rate=280)

if __name__ == "__main__":
    main()
