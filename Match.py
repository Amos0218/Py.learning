from collections import defaultdict

n = int(input())
t_card = list(map(int, input().split()))
s_card = list(map(int, input().split()))

# 儲存 s_card 中每個數字的所有索引
index_map = defaultdict(list)
for i, num in enumerate(s_card):
    index_map[num].append(i)

result = []
for i in range(n):
    target = t_card[i]
    if target in index_map:
        # 計算所有可能的索引差，取最小值
        min_diff = min(abs(i - j) for j in index_map[target])
        result.append(min_diff)
    else:
        result.append(-1)

print(' '.join(map(str, result)))