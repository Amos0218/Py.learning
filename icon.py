def draw_icon(L, W):
    # 初始化 L x L 矩陣，填充空白
    matrix = [[' ' for _ in range(L)] for _ in range(L)]

    # 初始邊長
    length = L

    # 定義四個方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0  # 目前方向，初始為右
    x, y = 0, 0  # 初始位置 (0, 0)

    # 當邊長大於 0 時繼續畫
    while length > 0:
        for _ in range(length):
            # 確保 (x, y) 在有效範圍內
            if 0 <= x < L and 0 <= y < L:
                matrix[x][y] = '*'
            # 移動到下一個位置
            x, y = x + directions[direction_index][0], y + directions[direction_index][1]

        # 轉彎（順時針）
        direction_index = (direction_index + 1) % 4
        
        # 每畫完水平或垂直邊，縮小邊長
        if direction_index == 0 or direction_index == 2:
            # 根據筆刷寬度 W，減少邊長
            length -= (2 if W == 2 else 1)

        # 防止在邊界縮小時繼續畫出界外的部分
        if length <= 0:
            break

    # 輸出矩陣
    for row in matrix:
        print(''.join(row))

# 讀取輸入
L, W = map(int, input().split())
draw_icon(L, W)