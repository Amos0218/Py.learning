x, r, v = map(int, input().split())  
n = int(input())  
practices = []


for _ in range(n):
    place, speed = map(int, input().split())
    practices.append((place, speed))

# 進行每次的躲避球練習
for place, speed in practices:
    if place < (x - r) or place > (x + r):  # 如果球不在接球範圍內
        continue  # 不動，跳過這次練習
    elif x - r <= place <= x + r and speed <= v:  # 如果在範圍內且球速合適
        x = place  # 接球，移動到球的位置
    elif place < x:  
        x += 15
    elif place > x:  
        x -= 15
    else:  # 如果球在阿茂的位置正好，閃躲到左邊
        x -= 15

print(x)  