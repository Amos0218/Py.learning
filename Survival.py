n = int(input())
H = list(map(int,input().split()))
W = list(map(int,input().split()))
smallest = float('inf')
for i in range(n):
    if H[i]*W[i] < smallest:
        smallest = H[i]*W[i]
        r_h = H[i]
        r_w = W[i]

print(r_h,r_w)
    
