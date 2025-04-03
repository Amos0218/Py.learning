
a = int(input())
nums = list(map(int,input().split()))
for i in range(a):
    n = nums[i]
    if n % 3 == 0 and n % 2 == 0:
        nums[i] = 1
    elif (n%10) % 2 == 1 and n % 3 != 0 :
        nums[i] = 2
    elif (n**0.5) % 1 == n or (n % 7 != 0 and n % 2 == 0):
        nums[i] = 3
    else:
        nums[i] = 0

print(' '.join(map(str,nums)))