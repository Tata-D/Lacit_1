# Задание 1

print("Задание 1")
a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
if a > b:
    print("a больше b")
elif a < b:
    print("a меньше b")
elif a == b:
    print("числа a и b равны")

# Задание 2

print("Задание 2")
a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))
if a > b:
    print("a больше b")
elif a < b:
    print("a меньше b")
elif a == b:
    print("числа a и b равны")

# Задание 3

print("Задание 3")
S = '943587612'
print(' '.join(S))

# Задание 4

print("Задание 4")
N = int(input("Введите число: "))
W = N*2-1
A = [ ]

for x in range(W):
    A.append([ ])
    for y in range(W):
       K = N - abs(y+1-N) - abs(x+1-N)
       A[x].append( K if K > 0 else ' ')

for l in A:
    print(*l, sep = ' ')

print('------------- Способ 2 -----------------')

N = int(input("Введите число N: "))
for i in range(1, N+1):
    print((N-i)*"  ", end = " ")
    for j in range(1, i+1):
        print(j, end = " ")

    for j in range(i-1, 0, -1):
        print(j, end = " ")
    print()

for i in range(N-1, 0, -1):
    print((N-i)*"  ", end = " ")
    for j in range(1, i+1):
        print(j, end = " ")

    for j in range(i-1, 0, -1):
        print(j, end = " ")
    print()

# Задание 5

print("Задание 5")
N = int(input("Введите число N: "))

for i in range(1, N+1):
    print((N-i)*"  ", end = " ")
    for j in range(N, N-i, -1):
        print(j, end = " ")

    for j in range(N-i+2, N+1):
        print(j, end = " ")
    print()

for i in range(N-1, 0, -1):
    print((N-i)*"  ", end = " ")
    for j in range(N, N-i, -1):
        print(j, end = " ")

    for j in range(N-i+2, N+1):
        print(j, end = " ")
    print()

# Задание 8

print("Задание 8")
N = int(input("Введите номер класса: "))
if N >= 1 and N <= 4:
    print("Первая ступень")
elif N >= 5 and N <= 9:
    print("Вторая ступень")
elif N >= 10 and N <= 11:
    print("Третья ступень")

# Задание 9

print("Задание 9")
s = 'hfbkxnvbwl54719'
for i in s:
   print(ord(i))

# Задание 10

print("Задание 10")
s = 'hfbkxnvbwl54719'
print(sum(map(ord, s)))

# Задание 11

print("Задание 11")
D = {13: 'cat', 9: 'dog', 17: 'rabbit', 5: 'bird', 12: 'horse'}
print(sorted(D.values()))
print(sorted(D.items()))

# Задание 12

print("Задание 12")
spisok = [7, 4, 18, 24, 67, 43, 21, 9, 54, 13]
print("Заданный список: ", spisok)
A = int(input("Введите элемент: "))
i = 0
while i < len(spisok):
    if spisok[i] == A:
        print("Элемент ", A, " есть в списке")
        break
    i = i+1
else:
    print("Элемента ", A, " нет в списке")

# Задание 13

print("Задание 13")
spisok = [7, 4, 18, 24, 67, 43, 21, 9, 54, 13]
print("Заданный список: ", spisok)
A = int(input("Введите элемент: "))
i = 0
for i in spisok:
    if i == A:
        print("Элемент ", A, " есть в списке")
        break
    i = i+1
else:
    print("Элемента ", A, " нет в списке")