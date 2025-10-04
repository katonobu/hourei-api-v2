import os
import tempfile
try:
    import pyttsx3
    from pydub import AudioSegment
    from mutagen.mp3 import MP3
    from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK
except ModuleNotFoundError as e:
    pyttsx3 = None
    print('pyttsx3 module is not found. MakeMp3() will be in dry_run mode.')


class MakeMp3():
    def __init__(self):
        pass

    def init(self, dry_run = False):
        self.dry_run = pyttsx3 is None or dry_run == True
        if self.dry_run == False:
            self.engine = pyttsx3.init()
        else:
            self.engine = None

    def mp3_tts(self, file_path_name, texts, track_num=0, title_str="", artist_name_str="", album_name_str="", rate=200, additional_texts_objs = None):
        if file_path_name.endswith(".mp3") == False:
            file_path_name += ".mp3"
        if os.path.isdir(os.path.dirname(file_path_name)) == False:
            os.makedirs(os.path.dirname(file_path_name), exist_ok=True)
        if self.dry_run == False:
            with tempfile.TemporaryDirectory() as td:
#                print(f'  Generating {title_str}')

                wav_file = os.path.join(td, "tmp.wav")
                self.engine.setProperty('rate', rate)
                self.engine.save_to_file("\n".join(texts), wav_file)
                self.engine.runAndWait()
                text_audio = AudioSegment.from_mp3(wav_file)
                combined = text_audio
                os.remove(wav_file)


                for idx, additional_texts_obj in enumerate(additional_texts_objs or []):
                    additional_texts = additional_texts_obj.get("texts", None)
                    mute_msec = additional_texts_obj.get("mute_msec", 0)

                    if 0 < mute_msec and additional_texts is not None:
                        mute_data = AudioSegment.silent(duration=mute_msec)
                        combined += mute_data

                        wav_file = os.path.join(td, f'tmp_{idx}.wav')
                        self.engine.setProperty('rate', rate)
                        self.engine.save_to_file("\n".join(additional_texts), wav_file)
                        self.engine.runAndWait()
                        text_audio = AudioSegment.from_mp3(wav_file)
                        combined += text_audio
                        os.remove(wav_file)

                combined.export(file_path_name, format='mp3')

                # タグを設定
                audio = MP3(file_path_name, ID3=ID3)
                kyokumei = title_str
                if rate != 200:
                    baisoku = rate/200
                    kyokumei = f"{title_str} {baisoku:1.1f}倍速"
                if 0 < len(title_str):
                    audio.tags.add(TIT2(encoding=3, text=kyokumei))   # 曲名
                if 0 < len(artist_name_str):
                    audio.tags.add(TPE1(encoding=3, text=artist_name_str)) # アーティスト
                if 0 < len(album_name_str):
                    audio.tags.add(TALB(encoding=3, text=album_name_str))  # アルバム
                if 0 < track_num:
                    audio.tags.add(TRCK(encoding=3, text=f"{track_num}"))  # トラック番号
                print(f'アーティスト名:{artist_name_str}, アルバム名:{album_name_str}, 曲名:{kyokumei}, トラック番号:{track_num}')
                audio.save()                
        else:
            total_texts = texts
            for idx, additional_texts_obj in enumerate(additional_texts_objs or []):
                additional_texts = additional_texts_obj.get("texts", None)
                mute_msec = additional_texts_obj.get("mute_msec", 0)
                if 0 < mute_msec and additional_texts is not None:
                    total_texts += f'[{mute_msec}ms silence]'
                    total_texts += additional_texts
            with open(file_path_name.replace(".mp3",".txt"), "w", encoding='utf-8') as f:
                f.write('\n'.join(total_texts))
            kyokumei = title_str
            if rate != 200:
                baisoku = rate/200
                kyokumei = f"{title_str} {baisoku:1.1f}倍速"
            print(f'  [dry_run] アーティスト名:{artist_name_str}, アルバム名:{album_name_str}, 曲名:{kyokumei}, トラック番号:{track_num}')

    
    def finish(self):
#        print("Finish MakeMp3().")
        if self.dry_run == False:
            self.engine.stop()
            self.engine = None


if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__),"mp3_test")
    mk_mp3 = MakeMp3()
    mk_mp3.init(dry_run=False)
    mk_mp3.mp3_tts(os.path.join(base_dir, "test1.mp3"), ["これはテストです。","Hello, this is a test."], track_num=1, title_str="テスト1", artist_name_str="テスト太郎", album_name_str="テストアルバム", rate=200)
    mk_mp3.mp3_tts(os.path.join(base_dir, "test2.mp3"), ["これはテストです。","Hello, this is a test."], track_num=2, title_str="テスト2", artist_name_str="テスト太郎", album_name_str="テストアルバム", rate=250, 
                   additional_texts_objs=[
                       {"texts":["1秒の無音の後に追加のテキストです。","This is additional text after a few seconds of silence."],"mute_msec":1000}
                    ])
    mk_mp3.mp3_tts(os.path.join(base_dir, "test3.mp3"), ["これはテストです。","Hello, this is a test."], track_num=2, title_str="テスト3", artist_name_str="テスト太郎", album_name_str="テストアルバム", rate=150, 
                   additional_texts_objs=[
                       {"texts":["1.5秒の無音の後に追加のテキストです。","This is additional text after a few seconds of silence."],"mute_msec":1500},
                       {"texts":["2秒の無音の後に追加のテキストです。","This is additional text after a few seconds of silence."],"mute_msec":2000}
                    ])
    mk_mp3.finish()
