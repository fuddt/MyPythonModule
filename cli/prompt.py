from typing import Callable


class Prompt:
    """プロンプトを生成するクラス"""
    def __init__(
        self,
        message: str,
        choices: list[str],
        output: Callable,
        attention: list[str] | str | None = None,
        go_back: bool = False,
    ):
        """Promptクラスのコンストラクタ

        Args:
            message (str): 質問内容
            choices (list[str]): 選択肢
            output (Callable): 選択肢を格納するオブジェクトに入力値を設定する関数を入れる
            attention (list[str] | str | None, optional): 注意事項があれば指定する.
            go_back (bool, optional): 1つ前に戻る選択肢を表示するかどうか. 
        """
        self.message = message
        self.choices = choices
        self.output = output
        self.attention = attention
        self.go_back = go_back
        self._validate_types()

    def _validate_types(self):
        """各属性のデータ型をチェックする関数"""
        if not isinstance(self.message, str):
            raise TypeError(f"message must be a str, got {type(self.message).__name__}")
        if not isinstance(self.choices, list) or not all(isinstance(choice, str) for choice in self.choices):
            raise TypeError("choices must be a list of strings")
        if not isinstance(self.go_back, bool):
            raise TypeError(f"go_back must be a bool, got {type(self.go_back).__name__}")
        if self.attention is not None:
            if not isinstance(self.attention, (str, list)):
                raise TypeError("attention must be a string or a list of strings")
            if isinstance(self.attention, list) and not all(isinstance(item, str) for item in self.attention):
                raise TypeError("attention list must contain only strings")
        if not callable(self.output):
            raise TypeError(f"output must be a callable, got {type(self.output).__name__}")

    def ask(self):
        print(self.message)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
        if self.attention:
            if isinstance(self.attention, str):
                print(self.attention)
            else:
                print("\n".join(self.attention))
        if self.go_back:
            print("r: 1つ前に戻る")

        while True:
            response = input("入力値: ")
            try:
                if response == "r":
                    return False
                choice = self.choices[int(response) - 1]
            except ValueError:
                print("無効な選択です")
            except IndexError:
                print("入力値が選択可能範囲を超えています")
            else:
                self.output(choice)
                return True
            finally:
                print("")


class PromptController:
    """プロンプトを管理するクラス"""
    def __init__(self):
        self.prompts = []
        self.current_prompt_index = 0
        
    def add_prompt(self, prompt: Prompt) -> None:
        self.prompts.append(prompt)

    def _confirm(self, obj: Callable) -> None:
        # 確認用のプロンプトを生成
        print("以下の内容でよろしいですか？")
        obj()
        print("y: はい / n: 最初に戻る / r: 1つ前に戻る")
        while True:
            response = input("入力値: ")
            if response == "y":
                break 
            elif response == "n":
                self.current_prompt_index = 0
                break 
            elif response == "r":
                self.current_prompt_index -= 1
                break 
            else:
                print("無効な選択です")
                
    def run(self, confirm_dialog: Callable | None = None) -> None:
        if self.prompts[0].go_back:
            raise ValueError("The first prompt cannot have go_back=True")

        while self.current_prompt_index < len(self.prompts):
            prompt = self.prompts[self.current_prompt_index]
            if prompt.ask():
                self.current_prompt_index += 1
            else:
                if self.current_prompt_index > 0:
                    self.current_prompt_index -= 1

            if self.current_prompt_index == len(self.prompts) and confirm_dialog is not None:
                self._confirm(confirm_dialog)

if __name__ == "__main__":
    # サンプルコード
    # 今日の1日のご飯を決めるプロンプト
    # まずはユーザーの入力値を受け取るクラスを作成
    
    class TodayMenu:
        def __init__(self):
            self.morning = None
            self.lunch = None
            self.dinner = None
        
        def set_morning(self, morning):
            self.morning = morning
        
        def set_lunch(self, lunch):
            self.lunch = lunch
        
        def set_dinner(self, dinner):
            self.dinner = dinner
    
        def today_menu(self):
            print(f"朝食: {self.morning}")
            print(f"昼食: {self.lunch}")
            print(f"夕食: {self.dinner}")
            
    # 上記を関数にまとめて、さらに入力値を返すようにする
    def get_today_menu():
        today_menu = TodayMenu()
        prompt_controller = PromptController()
        prompt_controller.add_prompt(Prompt("朝食は何にしますか？", ["トースト", "ご飯", "パンケーキ"], today_menu.set_morning))
        prompt_controller.add_prompt(Prompt("昼食は何にしますか？", ["カレー", "ラーメン", "サンドイッチ"], today_menu.set_lunch, go_back=True))
        prompt_controller.add_prompt(Prompt("夕食は何にしますか？", ["焼肉", "寿司", "天ぷら"], today_menu.set_dinner, go_back=True))
        prompt_controller.run(confirm_dialog=today_menu.today_menu)
        
        # 例えばjson形式で返す
        return {
            "morning": today_menu.morning,
            "lunch": today_menu.lunch,
            "dinner": today_menu.dinner
        }
    
    user_input_data = get_today_menu()
    print(user_input_data)