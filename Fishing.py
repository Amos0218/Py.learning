x,y = map(int,input().split())
n = int(input())
position = []
min_distance = float('inf')
for _ in range(n):
    a,b = map(int,input().split())
    position.append((a,b))

if n == 1:
    print(a,b)

for a,b in position:
    distance = (x - a)**2 + (y - b)**2
    if distance < min_distance:
        min_distance = distance
        closest = (a,b)

print(closest[0],closest[1])


