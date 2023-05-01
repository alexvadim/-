f=True
while(f==True):
 a=int(input("Введите число"))
 b=int(input("Введите число"))
 c=int(input("Введите число"))
 d=int(input("Выберите действие:1.Вывести минимальное число 2.Вывести максимальное число 3.Вывести среднее значение"))

 if d== 1:
    x = min(a,b,c)
    print(x)
 elif d== 2:
      x = max(a,b,c)
      print(x)
 elif d== 3:
      x = (a+b+c)/3
      print(x)
 else:
       break