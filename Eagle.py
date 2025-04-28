n = int(input())
chicken = list(map(int,input().split()))
E = int(input())
Q = int(input())
catched = list(map(int,input().split()))
for i in range(Q):
    #把被抓的雞在chicken的位置跟E交換
    chicken[chicken.index(catched[i])] = E
    E = catched[i]

print(*chicken)



    
