k, w, s, e = map(int, input().split())
total = 0

# 計算計程運價
if k <= 2:
    total += 20
else:
    total += 20 + (k - 2) * 5    

# 計算延滯費用
total += (w + 1) // 2 * 5

# 計算夜間加成
if e > 18:  # 確保有進入夜間加成時段
    s = max(s, 18)  # 如果上車時間早於 18:00，從 18:00 開始計算加成
    e = min(e, 23)  # 如果下車時間晚於 23:00，只計算到 23:00
    for hour in range(s, e):
        total += 185 + (hour - 18) * 10

print(total)