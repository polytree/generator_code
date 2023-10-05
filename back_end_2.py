from random import randrange
import random
from math import sqrt


def different(n):
    mas = [0, 0]
    if n % 2 == 0:
        mas[0] = [randrange(-n, n + 1, 2) for _ in range(1)][0]
        mas[1] = [randrange(-n, n + 1) for _ in range(1)][0]
    else:
        mas[0] = [randrange(-n + 1, n, 2) for _ in range(1)][0]
        mas[1] = [randrange(-n, n + 1) for _ in range(1)][0]
    a2 = random.sample(mas, 1)[0]
    if a2 == mas[0]:
        b1 = mas[1]
    else:
        b1 = mas[0]
    del mas
    m = 2 + a2 * b1 / 2
    c = m - 4
    # abs(c) = abs(a1 - b2)
    a1 = [randrange(-n, n + 1) for _ in range(1)][0]
    b2 = [a1 - c, a1 + c]
    if abs(b2[0]) < abs(b2[1]):
        b2 = int(b2[0])
    else:
        b2 = int(b2[1])
    lambda1 = ((a1 + b2) + sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
    lambda2 = ((a1 + b2) - sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
    if abs(b2) > n or lambda2 == lambda1 or b1 == 0:
        a1, b1, a2, b2, lambda1, lambda2 = different(n)
    return a1, b1, a2, b2, lambda1, lambda2


def similar(n):
    a1 = [randrange(-n, n + 1) for _ in range(1)]
    a1 = a1[0]
    b2 = [randrange(-n, n + 1) for _ in range(1)]
    b2 = b2[0]
    while (a1 - b2) ** 2 % 4 != 0 or a1 == b2:
        b2 = [randrange(-n, n + 1) for _ in range(1)]
        b2 = int(b2[0])
    a2b1 = int((a1 - b2) ** 2 / (-4))
    massive = [0, 0]
    per = random.sample(sample(a2b1), 1)[0]
    if per <= n:
        massive[0] = per
        massive[1] = int(a2b1 / massive[0])
        while abs(massive[0]) > n or abs(massive[1]) > n:
            massive[0] = random.sample(sample(a2b1), 1)[0]
            massive[1] = int(a2b1 / massive[0])
    else:
        massive[0] = per
        massive[1] = int(a2b1 / massive[0])
        while abs(massive[0]) > n or abs(massive[1]) > n:
            massive[0] = random.sample(sample(a2b1), 1)[0]
            massive[1] = int(a2b1 / massive[0])
    a2 = random.sample(massive, 1)[0]
    if a2 == massive[0]:
        b1 = massive[1]
    else:
        b1 = massive[0]
    del massive
    lambda1 = ((a1 + b2) + sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
    lambda2 = ((a1 + b2) - sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
    return a1, b1, a2, b2, lambda1, lambda2


def complex_diff(n):
    a1 = [randrange(-n, n + 1) for _ in range(1)][0]
    b2 = [randrange(-n, n + 1) for _ in range(1)][0]
    a2 = [randrange(-n, n + 1) for _ in range(1)][0]
    b1 = [randrange(-n, n + 1) for _ in range(1)][0]
    while (a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1) >= 0 or \
            abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1)) > 500 or b1 == 0:
        a1 = [randrange(-n, n + 1) for _ in range(1)][0]
        b2 = [randrange(-n, n + 1) for _ in range(1)][0]
        a2 = [randrange(-n, n + 1) for _ in range(1)][0]
        b1 = [randrange(-n, n + 1) for _ in range(1)][0]
    if sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) != \
            round(sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1)))):
        lambda1, lambda2 = lambda_with_not(a1, a2, b1, b2)
    else:
        lambda1, lambda2 = lambda_with(a1, a2, b1, b2)
    return a1, b1, a2, b2, lambda1, lambda2


def lambda_with_not(a1, a2, b1, b2):
    mas = []
    i = 2
    r = abs((a1 + b2)**2 - 4 * (a1 * b2 - a2 * b1))
    while r != 1:
        while r % i == 0:
            r /= i
            mas.append(i)
        i += 1
    Im1 = 1
    Im2 = 1
    while mas:
        if len(mas) > 1:
            if mas[0] == mas[1]:
                Im1 *= mas[0]
                del mas[0:2]
            else:
                Im2 *= mas[0]
                del mas[0]
        else:
            Im2 *= mas[0]
            del mas[0]
    Im2 = str(Im2)
    Im1 = Im1 / 2
    if str(Im1).split(".")[1] == "0":
        Im1 = int(Im1)
    else:
        Im1 = float(Im1)
    a1b2 = str((a1 + b2) / 2)
    if str(a1b2).split(".")[1] == "0":
        a1b2 = str(int((a1 + b2) / 2))
    else:
        a1b2 = str((a1 + b2) / 2)
    if Im1 == 1:
        if a1b2 == "0":
            lambda1 = "\u221a" + Im2 + " " + "i"
            lambda2 = "-\u221a" + Im2 + " " + "i"
        else:
            lambda1 = a1b2 + " + " + "\u221a" + Im2 + " " + "i"
            lambda2 = a1b2 + " - " + "\u221a" + Im2 + " " + "i"
    else:
        if a1b2 == "0":
            lambda1 = str(Im1) + " \u221a" + Im2 + " " + "i"
            lambda2 = "-" + str(Im1) + " \u221a" + Im2 + " " + "i"
        else:
            lambda1 = a1b2 + " + " + str(Im1) + " \u221a" + Im2 + " " + "i"
            lambda2 = a1b2 + " - " + str(Im1) + " \u221a" + Im2 + " " + "i"
    return lambda1, lambda2


def lambda_with(a1, a2, b1, b2):
    if abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1)) % 2 == 0:
        Im = str(int(sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2))
    else:
        Im = str(float(sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2))
    a1b2 = str((a1 + b2) / 2)
    if str(a1b2).split(".")[1] == "0":
        a1b2 = str(int((a1 + b2) / 2))
    else:
        a1b2 = str((a1 + b2) / 2)
    if a1b2 == "0":
        lambda1 = Im + " " + "i"
        lambda2 = "-" + Im + " " + "i"
    else:
        lambda1 = a1b2 + " + " + Im + " " + "i"
        lambda2 = a1b2 + " - " + Im + " " + "i"
    return lambda1, lambda2


def sample(a):
    mas = []
    for i in range(1, abs(a)):
        if abs(a) % i == 0:
            mas.append(i)
    if abs(a) == 1:
        mas.append(abs(a))
        return mas
    mas.append(abs(a))
    return mas
