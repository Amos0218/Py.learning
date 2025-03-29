n, customers, price = map(int, input().split())
result = 0
initial_n = n  # 保留初始數量

discount_ranges = [
    (0.8, 0.5),
    (0.6, 0.6),
    (0.4, 0.8),
    (0.2, 0.9)
]

for percent, discount in discount_ranges:
    upper = int(initial_n * percent)   # 修正上界誤差
    lower = upper - (initial_n // 5)  # 計算下界

    if n < lower:  # 這個區間沒貨了，跳過
        continue

    # 計算可賣數量與折扣價
    available = min(customers, n - lower)
    discounted_price = int(price * discount)

    # 計算當前區間可以賣多少
    result += available * discounted_price

    # 更新商品與顧客數量
    n -= available
    customers -= available

    if customers <= 0:  # 如果顧客已買完，提早結束
        break

print(result)