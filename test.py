# Задача с числами контрольный вопрос 6

a = bin(8**2022 + 2**2020 - 17)
spisok = [b for b in str(a)]
coin = 0
for i in spisok:
    if i == "1":
        coin += 1
    else:
        pass
print(coin)
