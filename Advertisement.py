m,a = map(int,input().split())
power = list(map(int,input().split()))
for i in range(m):
    if a > power[i]:
        a += power[i]
    else:   
        break
print(a)     
   



    
