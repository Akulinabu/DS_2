# *** Циклы (операторы циклов)

# **** Операторы цикла while ***


num = 0

# while num < 10:
#     print (num)
#     num += 1 # num = num + 1





#  прерывание цикла

# while num < 10:
#     print (num)
#     num += 1

#     if num == 5: # если значение num станет равно 5, 
#         break # то прерываем цикл, вызвав инструкцию break 

# while True:
#     s = input ("Введите команду: ")

#     print (f"Вы ввели команду: {s}")

#     if s == "stop":
#         break 





#  *** Пропуск куска кода

# while True:
#     s = input ("Введите 'ДА':" )
#     if s != "ДА":
#         print ("Вы не ввели слово 'ДА'!!! :((")
#         continue # инструкция continue возвращает цикл в начало

#     print(f"Молодец! Ты ввел команду: {s}")

#     break

# my_dict= {}
# for idx in  range (5 , 10 ,2):
#     my_dict[[ind] =indx *10]

#г***Генеротор списка ***
#  my list = [num for num in range (10)]
#  my_list = [num ** 2 for num in range (10) if num >3]
#  print (my_list)

# *** класс enumerate() ***

date = ['a', 'b', 'c', 'd']

# print(list (enumerate(date)))

# for index, item in enumerate(date):
#     print (index, item)


#**** генератор словаря***

# my_dict = {i : i for i in ['A', 'B', 'c', 'd'] }

my_dict = {item.upper() : index *10 for index, item in enumerate(date) if index > 0 }


# print (my_dict)

# ***калькулятор с циклами ***

while True:
    cmd = None
    # вывод чисел
    num_list = []
    for n in range (2):
        num = int (input(f"Введите {n} число: "))
        num_list.append(num)

    # ввод команды
    while True:
        cmd = input ("Введите команду: ")
        if cmd not in {"stop", "+", "-", "*", "/"}:
            print("Вы ввели неправильную команду!!! :((((")
            continue
        else:
            break
    
    # обработка выключения
    if cmd == "stop":
        print("До свидание!")
        break
    # вычисление
    if cmd == "+":
        res = num_list[0] + num_list[1]
    elif cmd == "-":
        res = num_list[0] - num_list[1]
    elif cmd == "*":
        res = num_list[0] * num_list[1]
    elif cmd == "/":
        res = num_list[0] / num_list[1]

    if float is type (res):
        #  вывод результата
        print(f"Результат: {res:.4f}")
    else:
        print(f"Результат: {res:.4f}")