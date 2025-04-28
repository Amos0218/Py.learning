n = int(input())
m = list(map(int, input().split()))
cur = int(input()) - 1   # 目前位置的索引



while True:
    next_left = cur - 1
    next_right = cur + 1

    # 確認沒有超出邊界
    left_valid = next_left >= 0 and m[next_left] < m[cur]
    right_valid = next_right < len(m) and m[next_right] < m[cur]  

    # 兩邊都不能滑，跳出
    if not left_valid and not right_valid:
        break

    # 比較落差
    if right_valid and (not left_valid or m[next_right] < m[next_left]):
        if m[next_right] >= m[cur]:
            break
        cur = next_right
    else:
        if m[next_left] >= m[cur]:
            break
        cur = next_left

if m[cur-1] == m[cur]:
    cur -= 1
print(cur + 1)