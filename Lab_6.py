import math

# -------------------------- Задание 1 --------------------------

print("Задание 1")
spisok = [(x-1, x) for x in range(1, 20)]
print(spisok)

# -------------------------- Задание 2 --------------------------
  
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

# -------------------------- Задание 3 --------------------------

print("\n\nЗадание 3")
def f1(n):
    a = -1
    for i in range(0, n):
        a += 1 
        yield a

def f3(n):
    a = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0: 
            yield i
            if i*i != n:
                a.append(n/i)
    for k in reversed(a):
        yield k
N = [1, 2]

for i in f1(10):
    print(i, end = ' ')
    if i > 0: break

for i in f3(56):
    if not i in N:
       print (i, end = ' ')

# -------------------------- Задание 4 --------------------------

print("\n\nЗадание 4")
def f4(n):
    a = -1
    for i in range(0, n):
        a += 1 
        yield a

for i in f4(20):
    print(i, end = ' ')

# -------------------------- Задание 5 --------------------------

print("\n\nЗадание 5")
def f5(n):
    a = -1
    for i in range(0, n):
        a += 1 
        yield a

for i in f5(20):
    print(i, end = ' ')
    if i == 9: break