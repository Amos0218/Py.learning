n = int(input())
result = []
total = 0
for _ in range(n):
    number,day = map(int,input().split())
    if day > 100:
        result.append(number)
        total += (day - 100)*5

result.sort()
print(*result)
print(total)