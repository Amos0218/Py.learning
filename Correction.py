s1 = input().strip()
s2 = input().strip()
n = int(input())
for _ in range(n):
    old_c,new_c = input().split()
    s1 = s1.replace(old_c,new_c)

count = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1
print(count)        


