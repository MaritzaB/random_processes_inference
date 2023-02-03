import math


def compara(base, m):
    for n in range(m):
        if (base**n) < math.factorial(n):
            return n
    return -1


def inserta(x, lst, i):
    # Devuelve una lista resultado de insertar x
    # en la posicion i
    return lst[:i] + [x] + lst[i:]


def inserta_multiple(x, lst):
    # Devuelve una lista con el resultado de insertar x
    # en todas las posiciones de lst
    return [
        inserta(x, lst, i)
        for i in range(len(lst) + 1)
    ]


def permuta(c):
    # Calcula y devuelve una lista de todas las
    # permutaciones posibles que se pueden hacer
    # con los elementos contenidos en c
    if len(c) == 0:
        return [[]]
    return sum(
        [
            inserta_multiple(c[0], i)
            for i in permuta(c[1:])
        ],
        [],
    )


def sgn(p):
    # Cuenta el numero de inversiones en una permutacion
    # y calcula su signo
    count = 0
    i = -1
    a = []
    for k in range(len(p)):
        a = a + [p[k]]
    while i < len(a) - 2:
        i = i + 1
        if a[i] > a[i + 1]:
            aux = a[i]
            a[i] = a[i + 1]
            a[i + 1] = aux
            count = count + 1
            i = -1
            continue
    if count % 2 == 0:
        return "par"
    return "impar"
