n = int(input())
garden = list(map(int,input().split()))
count = 0
i = 0
while i < n:
    if garden[i] == 1:
        j = i+1
        while j < n and garden[j] != 1:
            j += 1
        if j < n:
            segment = garden[i+1:j]
            forbidden = set()
            # idx：在 segment 中的索引（第幾個元素）
            for idx,val  in enumerate(segment):
                if val ==9:
                    if idx -1 >= 0:
                        forbidden.add(idx - 1)
                    if idx + 1 < len(segment):
                        forbidden.add(idx + 1)
            for idx ,val in enumerate(segment):
                if val == 0 and idx not in forbidden:
                    count += 1        
            i = j #從這個 1 往後繼續
        else:
            break
    else:
        i += 1            
print(count)        