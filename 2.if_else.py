# логические операторы

x = 6
y = 5

# res = x != y # оператор "не равно"

# res = x == y # оператор "равно"

# res = x < y # оператор "меньше"

res = x >= y # оператор "больше либо равно"

# print (f"\nрезультат: {res}")


z = True
k = False

# print (not k) # оператор "не" (инвентирующий оператор)

# print (z and k) # оператор И 

# print (z or k) # оператор ИЛИ

condition = z and (z or k)

# print (condition)



# УСЛОВНЫЕ ОПЕРАТОРЫ

a = 3

if a >= 5:
    c = "больше или равно 5"
elif a == 4:
    c = "равно 4"
elif a == 3:
    c = "равно 3"
else:
    c = "не равно ни чему"


# print (c)


b = 11

# if b > 0 and b < 10:
#    print ( "Лампочка ВКЛ" )
# else:
#    print ( "Лампочка ВЫКЛ" )

# класс тайп можно использовать совместно с инпут

# ***** ПРОСТЕНЬКИЙ КАЛЬКУЛЯТОР*****

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

operation = input ("Введите символ операции (+, -, *, /): ")

if operation == "+":
    res = num_1 + num_2
elif operation == "-":
    res = num_1 - num_2
elif operation == "*":
    res = num_1 * num_2
elif operation == "/":
    res = num_1 / num_2
else:
    res = "Введенный символ некорректный!!!"

print (f"Результат: {res}")

