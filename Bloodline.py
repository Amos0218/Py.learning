while True:
    try: n = int(input())
    except: break
    deg = [0]*n
    parent = [-1]*n
    height = [0]*n
    for i in range(n-1):
        s,t = map(int,input().split())
        parent[t] = s
        deg[s] += 1
    que = [v for v in range(n) if deg[v] == 0]
    front = 0
    diameter = 0
    while front < len(que):
        v = que[front];front += 1
        p = parent[v]
        if p < 0 :break
        diameter[p] = max(diameter,height[p] +height[v] + 1)    
        deg[p] -= 1
        if deg[p] == 0: que.append(p)
    print(diameter)     


        