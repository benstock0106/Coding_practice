from tkinter import BitmapImage


x = input('身高(公尺): ')
x = float(x)
y = input('體重(公斤): ')
y = float(y)
BMI = (y) / (x**2)
print('BMI:', BMI)
BMI = float(BMI)
if BMI < 18.5:
    print('體重過輕')
elif 18.5 <= BMI < 24:
    print('體重正常')
elif 24 <= BMI < 27:
    print('體重過重')
elif 27 <=BMI < 30:
    print('輕度肥胖')
elif 30 <= BMI < 35:
    print('中度肥胖')
else:
    print('重度肥胖')