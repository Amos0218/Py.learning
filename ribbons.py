m,n = map(int,input().split())
nums = list(map(int,input().split()))
beautiful = 0

color_count = {}    # 記錄當前窗口內的數字出現次數
left = 0

for right in range(n):      # 滑動窗口的右邊界
    #如果數字已經在字典裡，就+1 / 如果nums[right]還沒有出現在字典中，回傳0，再 +1
    color_count[nums[right]] = color_count.get(nums[right],0) + 1  

    # 如果窗口長度超過 m，則移除最左邊的元素
    if right - left + 1 > m:
        color_count[nums[left]] -= 1
        # 如果這個數字的計數變成 0，代表它已經完全不在窗口內，因此用 del 把它從字典中刪除
        if color_count[nums[left]] == 0:
            del color_count[nums[left]]

        left += 1

    if right - left + 1 == m and len(color_count) == m:
        beautiful += 1

print(beautiful)

# get() : 根據鍵獲取字典的「值」，若鍵不存在則返回默認值（預設是None）




