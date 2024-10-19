strk = str(input("Введите строку: ")) #запрос от пользователя строки
strk = strk.lower()  #нижний регистр
for i in range(len(strk)): #проверка каждого элемента
    if strk[i]=="е": #сравнение
        print(i) #вывод на экран