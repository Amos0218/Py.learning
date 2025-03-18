r, c = map(int, input().split())
grid = []

# 定義8個方向
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),         (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# 讀取輸入資料
for _ in range(r):
    row = list(map(int, input().split()))
    grid.append(row)

# 記錄被淘汰的人數
eliminated = 0

# 檢查每個位置是否被淘汰
for i in range(r):
    for j in range(c):
        current_flag = grid[i][j]
        all_different = True  # 預設此格子的八方鄰居都與它不同

        # 檢查 8 個方向
        for di, dj in directions:
            ni, nj = i + di, j + dj #計算 8 個方向的「鄰居座標」，以便進行比較與判斷
            if 0 <= ni < r and 0 <= nj < c:  # 確保不超出邊界
                if grid[ni][nj] == current_flag:
                    all_different = False
                    break     # 如果發現有相同的鄰居，就可以跳出這一輪檢查
        
        if all_different:     #確認完當前格子的八方都不同
            eliminated += 1

# 輸出被淘汰人數
print(eliminated)