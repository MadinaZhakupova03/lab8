import re

name = input("Введите ваше имя: ")

if name and re.match("^[a-zA-Z]+$", name):
    if name.istitle():
        print("Привет, " + name + "!")
    else:
        print("Пожалуйста, введите корректное имя.")
else:
    print("Пожалуйста, введите корректное имя.")

print("Спасибо за участие!")