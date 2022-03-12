# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小
# elif (另外如果)

import random
start = input('請輸入隨機數字範圍開始值: ')
end = input('請輸入隨機數字結束值: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('猜對有獎！請輸入數字： ')
    num = int(num)
    if r == num:
         print('終於猜對了')
         print('這是你猜得第', count, '次')
         break
    elif num > r:
        print('猜錯了,再猜小一點')
    elif num < r:
        print('猜錯了,再猜大一點')
    print('這是你猜得第', count, '次')