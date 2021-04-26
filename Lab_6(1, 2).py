import math

# Задание 1

print("Задание 1")
def f1(n):
    a = -1
    for i in range(0, n):
        a += 1 
        yield a

for i in f1(10):
    print(i, end = ' ')

# Задание 2

print("\nЗадание 2")
def f2(n):
    a = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0: 
            yield i
            if i*i != n:
                a.append(n/i)
    for k in reversed(a):
        yield k
    
for i in f2(56):
    print (i, end = ' ')

# Задание 3

print("\nЗадание 3")
