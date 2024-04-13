from datetime import datetime, timedelta

# 開始時刻と終了時刻を設定
start_time = datetime.strptime("09:00:00", "%H:%M:%S")
end_time = datetime.strptime("17:00:00", "%H:%M:%S")

# 1秒ごとに時刻を増加させてリストに保存
time_list = []
current_time = start_time
while current_time <= end_time:
    time_list.append(current_time.strftime("%H:%M:%S"))
    current_time += timedelta(seconds=1)

# 最初のいくつかの要素を表示して確認
time_list 
