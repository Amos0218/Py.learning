score = list(map(int,input().split()))

for i in range(6):
    table = list(map(int,input().split()))
    if score[i] == 0:
        print("X")
        continue

    if score[i] >= table[0]:
        print("A")
    elif score[i] >= table[1]:
        print("B")
    elif score[i] >= table[2]:
        print("C")
    elif score[i] >= table[3]:
        print("D")
    elif score[i] >= table[4]:
        print("E")  
    else:
        print("F")              