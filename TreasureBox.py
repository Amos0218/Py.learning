n = int(input())
box = list(map(int,input().split()))
X = float("inf")
Y = 0
Z = 0

for i in range(n):
    if box[i] <= X:
        X = box[i]
        index = i

if box.count(X) == 1:
    Y = box[index + X]
else:
    Y = box[index - X]

Z = box[Y - 1]
print(Z)



    
