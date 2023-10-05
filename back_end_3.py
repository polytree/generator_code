from back_end_2 import *


def calc(n):
    b_3 = [randrange(-n, n + 1) for _ in range(1)][0]
    c_2 = [randrange(-n, n + 1) for _ in range(1)][0]
    a_3 = [randrange(-n, n + 1) for _ in range(1)][0]
    c_1 = [randrange(-n, n + 1) for _ in range(1)][0]
    a2_b1 = -b_3 * c_2 - a_3 * c_1
    if a2_b1 == 0:
        mas = [0, [randrange(-n, n + 1) for _ in range(1)][0]]
        a_2 = random.sample(mas, 1)[0]
        if a_2 == mas[0]:
            b_1 = mas[1]
        else:
            b_1 = mas[0]
    else:
        a_2 = random.sample(sample(a2_b1), 1)[0]
        b_1 = int(a2_b1 / a_2)
    return b_3, c_2, a_3, c_1, a_2, b_1, a2_b1


def calc_complex(n):
    m = [randrange(1, 501) for _ in range(1)][0]
    b_3 = [randrange(-n, n + 1) for _ in range(1)][0]
    c_2 = [randrange(-n, n + 1) for _ in range(1)][0]
    a_3 = [randrange(-n, n + 1) for _ in range(1)][0]
    c_1 = [randrange(-n, n + 1) for _ in range(1)][0]
    a2_b1 = -b_3 * c_2 - a_3 * c_1 - m
    if a2_b1 == 0:
        mas = [0, [randrange(-n, n + 1) for _ in range(1)][0]]
        a_2 = random.sample(mas, 1)[0]
        if a_2 == mas[0]:
            b_1 = mas[1]
        else:
            b_1 = mas[0]
    else:
        a_2 = random.sample(sample(a2_b1), 1)[0]
        b_1 = int(a2_b1 / a_2)
    return b_3, c_2, a_3, c_1, a_2, b_1, a2_b1


def sys3_different(n):
    if n % 4 == 0:
        c3 = [randrange(-n, n + 1, 4) for _ in range(1)][0]  # c3 делится на 4
    elif n % 4 == 1:
        c3 = [randrange(-n + 1, n, 4) for _ in range(1)][0]  # с3 делится на 4
    elif n % 4 == 2:
        c3 = [randrange(-n + 2, n - 1, 4) for _ in range(1)][0]
    else:
        c3 = [randrange(-n + 3, n - 2, 4) for _ in range(1)][0]

    if (n - int(c3 / 4)) % 2 == 0:
        m = [randrange(-n - int(c3 / 4), n - int(c3 / 4), 2)][0]
    else:
        m = [randrange(-n - int(c3 / 4) + 1, n - int(c3 / 4) - 1, 2)][0]
    while m == 0:
        if (n - int(c3 / 4)) % 2 == 0:
            m = [randrange(-n - int(c3 / 4), n - int(c3 / 4), 2)][0]
        else:
            m = [randrange(-n - int(c3 / 4) + 1, n - int(c3 / 4) - 1, 2)][0]

    a1 = int(c3 / 4 + m / 2)
    b2 = int(c3 / 4 - m / 2)
    b3, c2, a3, c1, a2, b1, a2b1 = calc(n)

    iteration = 0
    d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + \
        a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
    while abs(a2) > n or abs(b1) > n or d != 0 or (a1 == b1 == c1 == 0)\
            or (a2 == b2 == c2 == 0) or (
            a3 == b3 == c3 == 0):
        if a2b1 == 0:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                mas = [0, [randrange(-n, n + 1) for _ in range(1)][0]]
                a2 = random.sample(mas, 1)[0]
                if a2 == mas[0]:
                    b1 = mas[1]
                else:
                    b1 = mas[0]
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
        else:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                a2 = random.sample(sample(a2b1), 1)[0]
                b1 = int(a2b1 / a2)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
    l1 = 0
    l2 = (-(a1 + b2 + c3) + sqrt(
        (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3
                                   - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
    l3 = (-(a1 + b2 + c3) - sqrt(
        (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3
                                   - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
    return a1, b1, c1, a2, b2, c2, a3, b3, c3, l1, l2, l3


def sys3_similar(n):
    if n % 4 == 0:
        c3 = [randrange(-n, n + 1, 4) for _ in range(1)][0]  # c3 делится на 4
    elif n % 4 == 1:
        c3 = [randrange(-n + 1, n, 4) for _ in range(1)][0]  # с3 делится на 4
    elif n % 4 == 2:
        c3 = [randrange(-n + 2, n - 1, 4) for _ in range(1)][0]
    else:
        c3 = [randrange(-n + 3, n - 2, 4) for _ in range(1)][0]

    a1 = int(c3 / 4)
    b2 = int(c3 / 4)
    b3, c2, a3, c1, a2, b1, a2b1 = calc(n)

    iteration = 0
    d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1\
        + a3 * b1 * c2 - a3 * b2 * c1
    while abs(a2) > n or abs(b1) > n or d != 0 or (a1 == b1 == c1 == 0)\
            or (a2 == b2 == c2 == 0) or (
            a3 == b3 == c3 == 0):
        if a2b1 == 0:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                mas = [0, [randrange(-n, n + 1) for _ in range(1)][0]]
                a2 = random.sample(mas, 1)[0]
                if a2 == mas[0]:
                    b1 = mas[1]
                else:
                    b1 = mas[0]
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
        else:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                a2 = random.sample(sample(a2b1), 1)[0]
                b1 = int(a2b1 / a2)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3\
                    + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
    l1 = 0
    l2 = (-(a1 + b2 + c3) + sqrt(
        (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3
                                   - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
    l3 = (-(a1 + b2 + c3) - sqrt(
        (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3
                                   - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
    return a1, b1, c1, a2, b2, c2, a3, b3, c3, l1, l2, l3


def sys3_complex(n):
    if n % 4 == 0:
        c3 = [randrange(-n, n + 1, 4) for _ in range(1)][0]  # c3 делится на 4
    elif n % 4 == 1:
        c3 = [randrange(-n + 1, n, 4) for _ in range(1)][0]  # с3 делится на 4
    elif n % 4 == 2:
        c3 = [randrange(-n + 2, n - 1, 4) for _ in range(1)][0]
    else:
        c3 = [randrange(-n + 3, n - 2, 4) for _ in range(1)][0]

    a1 = int(c3 / 4)
    b2 = int(c3 / 4)
    b3, c2, a3, c1, a2, b1, a2b1 = calc_complex(n)

    iteration = 0
    d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
    while abs(a2) > n or abs(b1) > n or d != 0 or (a1 == b1 == c1 == 0) or (a2 == b2 == c2 == 0) or (
            a3 == b3 == c3 == 0):
        if a2b1 == 0:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc_complex(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                mas = [0, [randrange(-n, n + 1) for _ in range(1)][0]]
                a2 = random.sample(mas, 1)[0]
                if a2 == mas[0]:
                    b1 = mas[1]
                else:
                    b1 = mas[0]
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
        else:
            if iteration == n:
                iteration = 0
                b3, c2, a3, c1, a2, b1, a2b1 = calc_complex(n)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                continue
            else:
                a2 = random.sample(sample(a2b1), 1)[0]
                b1 = int(a2b1 / a2)
                d = a1 * b2 * c3 - a1 * c2 * b3 - a2 * b1 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a3 * b2 * c1
                iteration += 1
    l1 = 0
    if sqrt(abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) != round(sqrt(
            abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1)))):
        l2, l3 = lambda_re_im(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    else:
        l2, l3 = lambda_re(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    return a1, b1, c1, a2, b2, c2, a3, b3, c3, l1, l2, l3


def lambda_re_im(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    mas = []
    i = 2
    r = abs((a1 + b2 + c3)**2 - 4*(a1*c3 + a1*b2 + b2*c3 - c2*b3 - a2*b1 - a3*c1))
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
    Im1 = str(Im1 / 2)
    a1b2c3 = str((a1 + b2 + c3) / 2)
    if str(a1b2c3).split(".")[1] == "0":
        a1b2c3 = str(int((a1 + b2 + c3) / 2))
    else:
        a1b2c3 = str((a1 + b2 + c3) / 2)
    if Im1 == "1.0":
        if a1b2c3 == "0":
            l1 = "\u221a" + Im2 + " " + "i"
            l2 = "-\u221a" + Im2 + " " + "i"
        else:
            l1 = a1b2c3 + " + " + "\u221a" + Im2 + " " + "i"
            l2 = a1b2c3 + " - " + "\u221a" + Im2 + " " + "i"
    else:
        if a1b2c3 == "0":
            l1 = Im1 + " \u221a" + Im2 + " " + "i"
            l2 = "-" + Im1 + " \u221a" + Im2 + " " + "i"
        else:
            l1 = a1b2c3 + " + " + Im1 + " \u221a" + Im2 + " " + "i"
            l2 = a1b2c3 + " - " + Im1 + " \u221a" + Im2 + " " + "i"
    return l1, l2


def lambda_re(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    if abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1)) % 2 == 0:
        Im = str(
            int(sqrt(abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) / 2))
    else:
        Im = str(
            float(sqrt(abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) / 2))
    a1b2c3 = str((a1 + b2 + c3) / 2)
    if str(a1b2c3).split(".")[1] == "0":
        a1b2c3 = str(int((a1 + b2 + c3) / 2))
    else:
        a1b2c3 = str((a1 + b2 + c3) / 2)
    l1 = a1b2c3 + " + " + Im + " " + "i"
    l2 = a1b2c3 + " - " + Im + " " + "i"
    return l1, l2
