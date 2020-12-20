
print("Введите температуру в градусах Цельсия")
n=int(input())
if n>=0:
    for i in range(0,n+1):
       b=(9*i/5)+32
       print(i,"     ",b)
else: print("Число должно быть неотрицательным")
   

