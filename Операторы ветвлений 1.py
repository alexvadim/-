f=True
while(f==True):
 a=int(input("Введите число"))
 b=int(input("Введите число"))
 c=int(input("Введите число"))
 d=int(input("Выберите действие:1.Вывести сумму чисел 2.Вывести произведение чисел"))

 if d== 1:
   x = a+b+c
   print(x)
 elif d== 2:
     x = a*b*c
     print(x)
 else:
     break