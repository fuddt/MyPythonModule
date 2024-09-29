"""
メールの文を作成するためのビルダーパターンのサンプルコード（Python）
メールの文を作成する際にもビルダーパターンを適用することで、メールの構成要素（件名、宛先、本文など）を段階的に組み立てることができます。
これにより、異なる種類のメールテンプレートを柔軟に扱うことが可能になります。
"""


class EmailBuilder:
    """メールの文を構築するためのビルダークラスです。"""

    def __init__(self):
        self.email = {"subject": "", "recipient": "", "body": ""}

    def set_subject(self, subject):
        """メールの件名を設定します。
        
        Args:
            subject (str): メールの件名。
        """
        self.email["subject"] = subject
        return self

    def set_recipient(self, recipient):
        """メールの宛先を設定します。
        
        Args:
            recipient (str): メールの宛先。
        """
        self.email["recipient"] = recipient
        return self

    def add_paragraph(self, text):
        """メール本文に段落を追加します。
        
        Args:
            text (str): 追加するテキスト。
        """
        self.email["body"] += f"{text}\n\n"
        return self

    def build(self):
        """最終的なメールを構築して返します。
        
        Returns:
            dict: 構築されたメールの内容。
        """
        return self.email

# クライアントコード
def main():
    email_builder = EmailBuilder()
    email = (email_builder.set_subject("Meeting Reminder")
                        .set_recipient("johndoe@example.com")
                        .add_paragraph("Dear John,")
                        .add_paragraph("This is a reminder about your upcoming meeting tomorrow at 10am.")
                        .add_paragraph("Best regards,")
                        .add_paragraph("Jane Doe")
                        .build())
    print(email)

if __name__ == "__main__":
    main()
