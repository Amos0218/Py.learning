n, s = map(int, input().split())  # 題數 N 和 每題分數 S
answer = list(input().split())    
m = int(input())      # 學生數量

# 儲存每位學生的答案
tuple_data = []

# 讀取答案
for _ in range(m):
    row = tuple(input().split())  # 學生的答案是字串型態，應該轉換為元組
    tuple_data.append(row)

# 計算每位學生的得分
for student_answers in tuple_data:
    correct = 0
    for i in range(n):  
        if student_answers[i] == answer[i]:  # 比較學生的答案與正確答案
            correct += 1
    print(correct * s)  # 得分等於正確題數 * 每題分數