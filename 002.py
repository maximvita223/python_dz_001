# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from unittest import result


list = ["X", "Y", "Z"]
list_a = []
for i in range(3):
    list_a.append(input(f"Введите значение {list[i]}: "))

left = not (list_a[0] or list_a[1] or list_a[2])
right = not list_a[0] and not list_a[1] and not list_a[2]
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
