import tkinter as tk
import glob
import os
from core.extractzip.extractzip import extract_file
from tkinter import filedialog
from tkinter import messagebox

def file_type_checker(filename):
    type1 = filename.endswith('.tar.gz')
    type2 = filename.endswith('.tgz')
    type3 = filename.endswith('.tar')
    type4 = filename.endswith('.gz')
    type5 = filename.endswith('.zip')

    if type1 or type2 or type3 or type4 or type5:
        return True
    else:
        return False


def browse_directory():
    choose_filename = filedialog.askopenfilename()
    directory_path = os.path.dirname(choose_filename)
    #実行を許可する
    if directory_path:
        filenames = glob.glob(os.path.join(directory_path,"*"))
        
        filename = [os.path.basename(i) for i in filenames if file_type_checker(i)]
        filename = '\n'.join(filename)
        response = messagebox.askyesno("実行確認", 
                                       f"{filename}\n\nこれらのファイルに処理を実行してもよろしいですか?\\n")
        
        if response:
            # メッセージを表示
            message_label.config(text="圧縮ファイルの解凍を実行中...")
            root.update()  # ウィンドウを更新
            extract_file(f"{directory_path}/*")
            # ここで実行する処理を追加
            message_label.config(text="処理が完了しました")
            messagebox.showinfo("実行結果", "完了しました。")
            
        else:
            messagebox.showinfo("実行結果", "キャンセルしました")


root = tk.Tk()
root.title("圧縮ファイルの解凍")
root.geometry("300x200")
root.resizable(True, True)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="フォルダの選択", command=browse_directory)
button.pack()
day_entry_label = tk.Label(root, text="注意\n選択したファイルと同じフォルダにある\nすべてのファイルに対して処理を実行します。")
day_entry_label.pack()
# メッセージ表示用のラベル
message_label = tk.Label(root, text="", fg="blue")
message_label.pack()

root.mainloop()

