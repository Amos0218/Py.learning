stk = []
child = [[] for _ in range(100005)]  #勿使用[]*100005
a = []

def stk_top(): return stk[-1]
def stk_push(x): stk.append(x)
def stk_pop(): stk.pop()

nodes = list(map(int,input().split()))
stk_push(nodes[0])  # 將第一個石室編號推入堆疊
a.append(nodes[0])  # 記錄訪問的第一個石室

for n in nodes[1:]:
    child[stk_top()].append(n)  # 把當前石室編號加入父石室的子石室列表
    if len(child[stk_top()]) == 2 + (stk_top() % 2):  # 判斷是否已經走完所有分支
        stk_pop()  # 如果是偶數石室編號，走完所有分支就退回上一層
    if n != 0:  # 如果不是死路，則繼續探索
        stk_push(n)
        a.append(n)

ans = 0
for i in a:
    for j in child[i]:
        if j == 0: continue  # 跳過死路
        ans += abs(i - j)  # 計算相鄰石室編號的絕對差並累加

print(ans)