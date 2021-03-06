# генератор паролей

from tkinter import Tk, StringVar, Label, Entry, Button
import hashlib as h

def hashing():
    """
    функция шифрования (хеширование)
    """
    # строка пароли
    origin_str=pwd.get()
    # кодировнаие в байт-строку
    byte_str=origin_str.encode()
    # шифрование - пропускание байт-строки через хеширование
    hash_str=h.sha256(byte_str)
    # преобразование в строку шестнадцатеричного числа (hex-числа)
    hex_str=hash_str.hexdigest()[:8]
    # передача хеш-строки 
    pwd_hash.set(hex_str)
    # print(hex_str)
    # print(type(byte_str))
# hashing()

# объект окна 
window=Tk()
# заголовок окна
window.title("Генератор паролей")
# переменные с объектами класса StringVar
pwd=StringVar()
pwd_hash=StringVar()

# Текстовая метка созданная виджетом (компонентом, элементом) класса Label
label=Label(text="Пароль: ")
# позиционирование виджета методом grid (сетка)
label.grid(row=0, column=0, padx=5, pady=5)
# Поле ввода строки, созданная виджетом Entry
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)
# Кнопка
Button(text="Click me", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# Поле вывода хеш-строки
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

window.mainloop()