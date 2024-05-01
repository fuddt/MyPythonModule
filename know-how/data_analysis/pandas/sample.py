# import pandas as pd
# import os

# def convert_to_date(month_day) -> str:
#     # 月と日に分割（整数を文字列に変換してからスライス）
#     month_day_str = str(month_day).zfill(4)  # 必ず4桁にするために0を補完
#     month = month_day_str[:2]
#     day = month_day_str[2:]
#     return f"{month}月{day}日"

# df = pd.read_csv(os.path.join(os.path.dirname(__file__),'./sample.csv'), index_col=0)
# df["MonthDay"] = df["MonthDay"].apply(convert_to_date)
# df.to_csv(os.path.join(os.path.dirname(__file__),'sample2.csv'), index=False)
