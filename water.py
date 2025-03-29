n, w = map(int, input().split())
day = -1
water = 0 
for i in range(n):
    data = list(map(int, input().split()))  # 讀取每一天的資料並轉換成整數列表
    a = data[0]  
    usage = sum(data[1:a+1])  # 計算當日總用水量

    water += w
    water -= usage  # 減去當日的總用水量

    if water < 0:  
        day = i + 1  
        break  
print()
print(day)  