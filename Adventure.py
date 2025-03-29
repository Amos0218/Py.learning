def turtle_adventure(n, heights, time):
    current_position = 0  
    while time > 0:
        # 確認還可以前進
        if current_position == n - 1:
            break
        
        # 找到當前區塊右邊的最大高度區塊
        max_height = max(heights[current_position + 1:])
        max_index = heights.index(max_height, current_position + 1)  # 找到最接近的最大區塊索引

        # 移動到該區塊
        time -= (max_index - current_position)  
        if time < 0:
            return current_position + 1  # 區塊的編號從一開始
        
        current_position = max_index

        # 抵達最右端，開始折返
        if current_position == n - 1:
            min_height = float('inf')  
            min_index = -1
            for i in range(1, current_position):  # 從經過的區塊中找最低的
                if heights[i] <= min_height:  # 修正條件，確保找到最近的最小值
                    min_height = heights[i]
                    min_index = i
            return min_index + 1  

    # 如果時間耗盡，回傳當前位置
    return current_position + 1  

        
    
n = int(input())
heights = list(map(int,input().split()))
time = int(input())

print(turtle_adventure(n,heights,time))


