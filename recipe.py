import math

N, A = map(int, input().split())  
recipe = list(map(int, input().split()))  

B = recipe[N]  
for i in range(N):
    recipe[i] *= (B / A)
    # float有精度問題，在無條件進位之前要先四捨五入
    recipe[i] = math.ceil(round(recipe[i],4))  


print(" ".join(map(str, recipe[:-1])))