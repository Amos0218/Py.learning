t,r = map(int,input().split())
target = t - (1+r) * int(t/(1+r))
if target <= r and target != 0:
    print(1)
else:
    print(0)    
 