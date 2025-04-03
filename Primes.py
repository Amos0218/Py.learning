import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def answer(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            j = n // i
            if is_prime(i) and is_prime(j):
                print(i,j)
                break
    else:
        print("0 0")     

            
n = int(input())
answer(n)
