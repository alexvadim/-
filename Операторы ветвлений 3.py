f = True
while(f==True):
 a=int(input("Введите длину метров"))
 b=int(input("Выберите действие 1.Перевести в дюймы 2.Перевести в мили 3.Перевести в ярды"))

 if b== 1:
    x = (a)*39.37
    print(x)
 elif b== 2:
      x = (a)*0.00062
      print(x)
 elif b== 3:
      x= (a)*1.09
      print(x)
 else:
     break