# Задача 5

a = input()

try:
    if len(a) <= 60:
        if a[-1] == ".":
            spisok = [b for b in str(a)]
            spisok.pop(-1)
            c = "".join(spisok)
            print(int(c, 2))
        else:
            spisok = [b for b in str(a)]
            c = "".join(spisok)
            print(int(c, 2))
    else:
        print("Слишком длинное число")
except ValueError:
    print("Введите число")
