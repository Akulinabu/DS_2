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
 
 my_list = [num ** 2 for num in range (10) if num >3]
 print (my_list)
