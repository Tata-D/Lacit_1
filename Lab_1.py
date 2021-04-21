# Задание 1

print("№ 1")
print('Lacit')

# Задание 2

print('№ 2')
print('Friday')
print('April')
print('Tatyana')

# Задание 3

print('№ 3')
i = '0'
print(i)
print(i*2)
print(i*3)
print(i*4)
print(i*5)

# Задание 4

print('№ 4')
print('*      *      *')
print(' *    * *    *')
print('  *  *   *  *')
print('    *     *')

# Задание 5

print('№ 5')
print(' _______________________')
print('|\t|\t|\t|')
print('|   4   |   9   |   2   |')
print('|_______|_______|_______|')
print('|\t|\t|\t|')
print('|   3   |   5   |   7   |')
print('|_______|_______|_______|')
print('|\t|\t|\t|')
print('|   8   |   1   |   6   |')
print('|_______|_______|_______|')

# Задание 6

print('№ 6')
print(' _______________________\n|\t|\t|\t|\n|   4   |   9   |   2   |\n|_______|_______|_______|\n|\t|\t|\t|\n|   3   |   5   |   7   |\n|_______|_______|_______|\n|\t|\t|\t|\n|   8   |   1   |   6   |\n|_______|_______|_______|')

# Задание 7

print('№ 7')
print(1/2+1/4)

# Задание 8

print('№ 8')
a = 2
b = 3
print((a+4*b)*(a-3*b)+a^2)

# Задание 9

print('№ 9')
x = -2
print(abs(x)+x**5)

# Задание 10.a

print('№ 10.a')
x = 1.7
print((x+1)**2+3*(x+1))

# Задание 10.b

print('№ 10.b')
x = 3
print((x+1)**2+3*(x+1))

# Задание 11

print('№ 11')
x = -2.34
print((abs(x-5)-math.sin(x))/3+math.sqrt(x**2+2014)*math.cos(2*x)-3)

# Задание 12

print('№ 12')
x = 3.6
print(math.exp(x-2)+abs(math.sin(x))-x**4*math.cos(1/x))

# Задание 13

print('№ 13')
a = 0.1
b = 0.2
x = 1
print((x**2+b)**(1/5)-(b**2*(math.sin(x+a))**3)/x)

# Задание 14

print('№ 14')
c = int(input("Введите номер месяца: "))
if c >= 1 and c <= 2 or c == 12:
    print("Зима")
elif c >= 3 and c <= 5:
    print("Весна")
elif c >= 6 and c <= 8:
    print("Лето")
elif c >= 9 and c <= 11:
    print("Осень")
else:
    print("Ошибка ввода данных")

# Задание 15

print('№ 15')
spisok = ["L", "a", "c", "i", "t", True, 7, 3.85]
print(spisok)

spisok.append(False)
print(spisok)

spisok.remove(3.85)
print(spisok)

spisok.reverse()
print(spisok)

print(" L\n", "a\n", "c\n", "i\n", "t\n", True, '\n', 7, '\n', 3.85, '\n')