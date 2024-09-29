"""
HTMLドキュメントジェネレーター用ビルダーパターンのサンプルコード（Python）
以下の例では、HTMLドキュメントを段階的に構築するためのビルダーパターンを実装しています。これにより、複雑なHTML構造も簡単に管理し、拡張することができます。
"""

class HTMLBuilder:
    """HTMLコンテンツを構築するためのビルダークラスです。"""
    
    def __init__(self):
        self.parts = []

    def add_title(self, title):
        """HTMLドキュメントにタイトルを追加します。
        
        Args:
            title (str): ドキュメントのタイトル。
        """
        self.parts.append(f"<title>{title}</title>")
        return self

    def add_heading(self, heading, level=1):
        """HTMLドキュメントに見出しを追加します。
        
        Args:
            heading (str): 見出しのテキスト。
            level (int): 見出しのレベル（h1, h2, ... h6）。デフォルトは1。
        """
        self.parts.append(f"<h{level}>{heading}</h{level}>")
        return self

    def add_paragraph(self, text):
        """HTMLドキュメントに段落を追加します。
        
        Args:
            text (str): 段落のテキスト。
        """
        self.parts.append(f"<p>{text}</p>")
        return self

    def build(self):
        """最終的なHTMLドキュメントを構築して返します。
        
        Returns:
            str: 完成したHTMLドキュメント。
        """
        return "<html>" + "".join(self.parts) + "</html>"

# クライアントコード
def main():
    builder = HTMLBuilder()
    html_content = (builder.add_title("My Document")
                           .add_heading("Welcome to My Document", level=1)
                           .add_paragraph("This is an example paragraph in our HTML document.")
                           .build())
    print(html_content)

if __name__ == "__main__":
    main()
