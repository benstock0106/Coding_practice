#題目 密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者(最多輸入三次密碼) 提示:while
#不對的話 就印出'密碼錯誤! 還有__次機會"
#對的話 就印出'登入成功'

password = 'a123456'
i = 3 #i代表剩餘機會
while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break #逃出迴圈
    else:
        i = i - 1
        print('密碼錯誤! 還有',i,'次機會')
        if i == 0:
            break