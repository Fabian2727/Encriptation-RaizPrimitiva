def mod(a, b):
    q = a//b
    r = a - b*q
    r = r + (r < 0) * b
    return r

def expM(a,b, n): #a = base, b = exponente, n = módulo
    if b == 1: 
        return mod(a,n)
    Nb = b//2
    res = expM(a,Nb,n)
    if b % 2: 
        return mod(res*res*a, n)
    return mod(res**2, n)

def isprime (a):
    if a < 1:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True         

def comparar (l1, l2): #l1 = la lista que almacena las expo. l2 = lista de referencia (a comparar)
    equal = False
    #print("####################################################")
    #print(l1)
    #print(l2)
    if len(l1) == len(l2):
        if min(l1) != 1:
            equal = False
        else:
            l1.sort()
            if (l1 == l2):
                equal = True
    return equal
    
def raizP (p):
    g = 2
    cont = 1
    res = 0
    list1 = []
    list2 = []
    if (isprime(p) == False):
        print("El numero ",p," no es primo. Ingrese un nuevo numero")
        return 0
    else:
        while (cont != p):
            res = expM(g,cont,p)
            cont = cont + 1
            list1.append(res)
            list2.append(cont-1)
        if comparar(list1, list2) == False:
            g = g+1
            raizP(p)
        else:
            print("La raiz primitiva de ",p," es: ",g)
            return g

raizP(181)
