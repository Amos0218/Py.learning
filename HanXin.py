nums = []
for _ in range(3):
    a,b = map(int,input().split())
    nums.append((a,b))
x = 1
while True:
    if x % nums[0][0] == nums[0][1] and x % nums[1][0] == nums[1][1] and x % nums[2][0] == nums[2][1]:
        print(x)
        break
    x += 1
    


