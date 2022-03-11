#題目 密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者(最多輸入三次密碼) 提示:while
#不對的話 就印出'密碼錯誤! 還有__次機會"
#對的話 就印出'登入成功'

password = 'a123456'
x = 3 # 設x為剩餘機會
while x > 0:
    x = x - 1
    pwd = input('請輸入密碼：')
    if pwd == password:
        print('成功登入')
        break
    else:
        if x > 0:
            print('密碼錯誤', x, '次機會')
        else:
            print('沒機會嘗試了!要鎖帳號了')
