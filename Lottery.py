lucky = list(map(int,input().split()))
number = list(map(int,input().split()))
money = list(map(int,input().split()))
result = 0
i = 0
for i in range(2):
    if lucky[i] in number:
        result += money[number.index(lucky[i])]
    i += 1
if lucky[2] not in lucky[:2]:    #第三個不等於第一個或第二個
    if lucky[2] in number:
        result -= money[number.index(lucky[2])]       
        result = max(result,0)
    else:
        result *= 2

print(result)
