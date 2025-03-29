s,e,b,k = map(int,input().split())
count = 0
number = -1

for i in range(s,e+1):
    if i % b == 0 or str(b) in str(i):
        count += 1
        if count == k:
            number = i
            break
     

print(number)

