import random

# Problem 1
def largerIndex(c):
    k = []
    for i in range(len(c)):
        if c[i] > i:
            k.append(1)
        elif c[i] == i:
            k.append(0)
        else:
            k.append(-1)
    return k


# Problem 2
def squareUpTo(n):
    l = []
    i = 0
    while i ** 2 <= n:
        l.append(i ** 2)
        i += 1
    return l


# Problem 3
def flip1in3():
    while True:
        coin1 = random.randint(0, 1)
        coin2 = random.randint(0, 1)
        if coin1 == 1:
            return False
        elif coin2 == 1:
            return True

# Problem 4
def duplicates(c):
    dup = []
    for i in c:
        if sum([n == i for n in c]) == 2 and (i not in dup):
            dup.append(i)
    return dup