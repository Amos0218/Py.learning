def classify_number(n):
    while n > 10:
        nums = list(map(int,str(n)))
        length = len(nums)
        if length == 4:
            left = nums[:2]
            right = nums[2:]
            if right[0] == 0:
                right_value = right[1]
            else:
                right_value = right[0]*right[1] if len(right) == 2 else right[0]

            left_value = left[0]*left[1] if len(left) == 2 else left[0]
            
            n = int(str(left_value) + str(right_value))

        elif length == 3:
            x = nums[0] * nums[1]
            y = nums[1] * nums[2]
            n = int(str(x) + str(y))

        elif length == 2:
            n = nums[0]*nums[1]     
    return n

n = int(input())
print(classify_number(n))

        



