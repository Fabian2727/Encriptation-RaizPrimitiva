def mod(a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r


def calcular (b,m,res):
    expo = 1
    aux = mod(b**expo,m)
    while (aux != res):
        expo = expo +1
        aux = mod(b**expo,m)
    return expo


print(calcular(6,100049,2021))
