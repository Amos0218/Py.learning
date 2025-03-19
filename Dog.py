from collections import deque

# BFS 來遍歷所有可達的格子
def bfs(start_x, start_y, n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上、下、左、右
    visited = [[False] * n for _ in range(n)]  # 記錄是否已經遍歷過（初始化為False)
    queue = deque([(start_x, start_y)])  # 儲存需要遍歷的格子
    visited[start_x][start_y] = True
    reachable_count = 1  # 起始位置已經是可達的格子

    while queue:
        x, y = queue.popleft()  # 使得BFS遍歷符合先進先出的行為（從最左拿）

        # 遍歷上下左右的座標
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 檢查是否在範圍內且還沒被遍歷過
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 檢查高度差
                if abs(grid[nx][ny] - grid[x][y]) <= 2:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    reachable_count += 1

    return reachable_count


def main():
    # 輸入處理
    n = int(input())  
    start_x, start_y = map(int, input().split())  # 最後一次看到狗的座標
    grid = [list(map(int, input().split())) for _ in range(n)]  # 建構地圖

    # 計算可達格子數量
    result = bfs(start_x, start_y, n, grid)
    
    print(result)

if __name__ == "__main__":
    main()


