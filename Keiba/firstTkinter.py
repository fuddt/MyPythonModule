import tkinter as tk
from combination import TicketCombination

"""
出走頭数入力欄:
馬券の種類入力欄:
[計算ボタン]

|-----------|
|出力エリア   |
|           |
|           |
|-----------

"""
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #フレームの作成
        master.title("馬番組み合わせの計算")
        master.geometry("600x450+400+200")

        #部品の作成
        label = tk.Label(text="頭数")
        self.horses = tk.Entry()
        label2 = tk.Label(text="馬券の種類")
        self.ticket_types = tk.Entry()
        self.output_area = tk.Text()
        self.button = tk.Button(text="計算",command= self.action_event)
        #設置
        [widget.pack() for widget in (label, self.horses, label2, self.ticket_types, self.button, self.output_area)]

    def action_event(self):
        #フィールドの初期化
        if len(self.output_area.get(0.0,tk.END)) > 0:
            self.output_area.delete(0.0,tk.END)
        horse_num = self.horses.get()
        ticket_type = self.ticket_types.get()
        method = self.methods(ticket_type)
        combinations = method(horse_num)
        for index, combination in enumerate(combinations):
            i = f"{index+1}.0"
            combi = f"{combination}\n"
            self.output_area.insert(i,combi)

    def methods(self, ticket_type: str)-> object:
        ticket_type = ticket_type.strip()
        tc = TicketCombination()
        methods_dict = {
            "枠連":tc.combination_bracket,
            "馬単":tc.combination_exacta,
            "馬連":tc.combination_quinella,
            "3連複":tc.combination_trio,
            "3連単":tc.combination_trifecta
        }
        return methods_dict[ticket_type]

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()