# Задание 1, 2
print("Задание 1, 2")
def f(a,b):
    if a > b:
       print("a больше b")
    elif a < b:
       print("a меньше b")
    elif a == b:
       print("числа a и b равны")
       
f(3,7)
f(14,8)
f(9,9)
f(3.5,8.2)

# Задание 3

print("Задание 3")
def f(S):
   print(' '.join(S))

f(S = '943587612')

# Задание 4
print("Задание 4")
def f(N):
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

f(5)

# Задание 5
print("Задание 5")
def f(N):
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

f(7)

# Задание 8
print("Задание 8")
def f(N):
   if N >= 1 and N <= 4:
       print("Первая ступень")
   elif N >= 5 and N <= 9:
       print("Вторая ступень")
   elif N >= 10 and N <= 11:
       print("Третья ступень")

f(3)
f(11)
f(7)

# Задание 9
print("Задание 9")
def f(s):
   for i in s:
      print(ord(i))

f(s = 'hfbkxnvbwl54719')

# Задание 10
print("Задание 10")
def f(s):
   print(sum(map(ord, s)))

f(s = 'hfbkxnvbwl54719')

# Задание 11
print("Задание 11")
def f(D):
   print(sorted(D.values()))
   print(sorted(D.items()))

f(D = {13: 'cat', 9: 'dog', 17: 'rabbit', 5: 'bird', 12: 'horse'})

# Задание 12
print("Задание 12")
def f(spisok):
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

f(spisok = [7, 4, 18, 24, 67, 43, 21, 9, 54, 13])

# Задание 13
print("Задание 13")
def f(spisok):
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

f(spisok = [7, 4, 18, 24, 67, 43, 21, 9, 54, 13])