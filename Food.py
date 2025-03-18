while True:
    try:
        # 讀取初始的守衛數量 (guard) 和每位守衛的最大食物消耗量 (b)
        guard, b = map(int, input().split())

        # 總食物量 = 守衛數量 * 每人離開前消耗的食物量
        food = guard * b

        day = 0  # 記錄經過的天數
        minus = 0  # 累積的食物消耗量 (用來判斷何時有守衛離開)

        while food > 0:  # 當食物還有剩時，繼續模擬
            day += 1  # 過了一天
            food -= guard  # 當前所有守衛一起消耗食物
            if food <= 0:  # 如果食物消耗完，直接結束
                break

            minus += guard  # 累積消耗的食物

            # 判斷是否有守衛要離開
            while minus >= b and guard > 0:
                guard -= 1  # 有一名守衛離開
                minus -= b  # 扣除該守衛的累積食物消耗

        print(day)  # 印出守衛能夠存活的天數

    except:
        break  # 當輸入結束 (EOF) 或發生錯誤時，跳出迴圈