#5
a = int(input("Расстояние в км: "))
b = int(input("Расход топлива в литрах: "))
c = int(input("Стоимость литра: "))
top = a * b
rub = top*c
print(f"Топливо: {top} л")
print(f"Стоимость: {rub} руб")

