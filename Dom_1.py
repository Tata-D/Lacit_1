# Задание 1
print("Задание 1")
spisok = [3, 4, 7 ,9, 2, 8, 1, 6]
new_spisok = [x for x in spisok if x % 2 == 0]
print(new_spisok)

# Задание 2
print("Задание 2")
spisok = [8, 3, 9, 2, 1, 7, 5]
new_spisok = spisok[0::2]
print(new_spisok)

# Задание 3
print("Задание 3")
spisok = [2, -6, 9, 1, -3, -15, 7, -17]
new_spisok = [x for x in spisok if x > 0]
print(new_spisok)

# Задание 4
print("Задание 4")
spisok = [3, 6, 8, 1, 7, 4, 2]
m = int(input("Введите делитель: "))
print([{x for x in spisok if x % m == i} for i in {x % m for x in spisok}])

# Задание 5
print("Задание 5")
D = {8:7, 4:9, 'a':5, 6:3, 2:'a'}
print([i + D[i] for i in D if type(i) != str and type(D[i]) != str])

# Задание 6
print("Задание 6")
spisok = [8, 3, 6, 7, 9, 2, 17, 13]
print([(spisok[i], spisok[j]) for i in range (len(spisok)) for j in range (len(spisok)) if spisok[i] < spisok[j]])

# Задание 7
print("Задание 7")
spisok = [3, 6, 8 ,1, 5, 2, 17, 9, 7, 13]
print({spisok[i]: spisok[i+1] for i in range(0, len(spisok), 2)})
