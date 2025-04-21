x,y,L,R = map(int,input().split())
N = int(input())
count = 0
for _ in range(N):
    s_x,s_y,s_L = map(int,input().split())
    if (s_x - x)**2 + (s_y - y)**2 <= R**2:
        if s_L <= L:
            count += 1

print(count)

        
