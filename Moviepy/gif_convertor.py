from moviepy.editor import VideoFileClip
import os
from PIL import Image

# PILのImageモジュールのANTIALIASをLANCZOSに置き換え
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.LANCZOS

# 動画ファイルのパス
video_path = input("Enter the path of the video file: ")

# 入力されたパスにダブルクォーテーションが含まれている場合は削除
if '"' in video_path or "'" in video_path:
    video_path = video_path.replace('"', '').replace("'", '')

if not os.path.exists(video_path):
    print("The file does not exist.")
    exit()

# 出力するGIFファイルに変換する
# 元のファイル名の'.'以降を削除して、拡張子をgifに変更
gif_path = os.path.splitext(video_path)[0] + '.gif'

# 動画クリップを読み込み
clip = VideoFileClip(video_path)

# ユーザーに以下の選択を聞く
# 1. 全体をGIFに変換
# 2. 一部を切り取ってGIFに変換　（例えば、10秒から20秒まで）

print("1. Convert the entire video to a GIF")
print("2. Convert a part of the video to a GIF")

choice = input("Enter the number of the option you want to choose: ")

while True:
    if choice == "1":
        break
    elif choice == "2":
        while True:
            try:
                start_time = int(input("Enter the start time (seconds): "))
                end_time = int(input("Enter the end time (seconds): "))
                if start_time < 0 or end_time > clip.duration or start_time >= end_time:
                    raise ValueError("Invalid time range.")
                clip = clip.subclip(start_time, end_time)
                break
            except ValueError as e:
                print(e)
                print("Please enter valid start and end times.")
        break
    else:
        print("Invalid input.")
        choice = input("Enter the number of the option you want to choose: ")

# リサイズするかどうかをユーザーに聞く
resize_choice = input("Do you want to resize the video? (yes/no): ").strip().lower()

if resize_choice == "yes":
    while True:
        try:
            resize_factor = float(input("Enter the resize factor (e.g., 0.5 for 50%): "))
            if resize_factor <= 0 or resize_factor > 1:
                raise ValueError("Resize factor must be between 0 and 1.")
            clip = clip.resize(resize_factor)
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid resize factor.")
elif resize_choice != "no":
    print("Invalid input. Proceeding without resizing.")

# フレームレートを設定してGIFに変換
# ask the user for the frame rate
frame_rate = input("Do you want to set the frame rate? (yes/no): ").strip().lower()

if frame_rate == "yes":
    while True:
        try:
            fps = int(input("Enter the frame rate: "))
            clip = clip.set_fps(fps)
            if fps <= 0:
                raise ValueError("Frame rate must be greater than 0.")
            clip.write_gif(gif_path)
            break
        except ValueError as e:
            print(e)
            print("Please enter a valid frame rate.")
else:
    clip.write_gif(gif_path)

print(f"GIF has been saved as {gif_path}")
