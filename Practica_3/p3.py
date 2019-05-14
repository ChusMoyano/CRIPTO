#Alumnos 
# Manuel Ruiz López
# Pablo García calvo
# Sergio 
# Jesús Moyano Doña
######################################################
##              Logaritmo Discreto                  ##
######################################################
import math
from random import randrange
from funciones_aux import *




"""
    Calcular | a^b mod m | de forma eficiente 

    Args:
        a   Número que hace de testigo
        b   Exponente del testigo
        m   Módulo del conjunto entero con el que trabajamos
    
    Returns:
        Resultado de a^b mod m
"""


def potenciaModular(a, b, m):
    aux = 1

    while b > 0:

        # si b es impar
        if b & 1:
            aux = (aux*a) % m

        # b / 2 truncando el acarreo
        b = b >> 1
        # a ^ 2
        a = (a * a) % m

    return aux

######################################################
###                 Fuerza bruta                   ###
######################################################


"""
    Sea p un número primo y sea a un entero tal que 2 <= a <= p-2
    b un número comprendido entre 1 y p-1, existe un x tal que a^x=b mod p?
    Si existe, x es el logaritmo en base a de b modulo p

    El algoritmo de fuerza busca 
"""


def fuerzaBruta(a, b, p):
    for x in range(p-1):
        if potenciaModular(a, x, p) == b:
            return x

    return False

#####################################################
###           Paso enano - paso gigante           ###
#####################################################


"""
    Busca un item dentro de una lista ordenada
    La lista está compuesta de pares y el item
    solo se busca en el primer elemento de cada par
    Devuelve el segundo elemento si lo encuentra, si no
    devuelve -1
"""


def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = -1

    while primero <= ultimo and encontrado == -1:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio][0] == item:
            encontrado = unaLista[puntoMedio][1]
        else:
            if item < unaLista[puntoMedio][0]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado


"""
    Criterio para ordenar una lista de pares solo por el primer elemento
"""


def sortCriteria(e):
    return e[0]


"""
    Algoritmo de factorización por Paso enano - Paso gigante
"""


def pasoEnanoPasoGigante(a, b, p):
    # Raíz cuadrada de p redondeada hacia arriba (s)
    s = math.ceil(math.sqrt(p))

    # Se obtiene la lista S siendo b el primer elemento
    # y multiplicando por a cada elemento hasta llegar
    # a s elementos
    S = []
    aux = b
    S.append([aux, 0])
    for x in range(1, s):
        aux = (aux*a) % p
        S.append([aux, x])

    # Se ordena la lista para realizar más rápido las búsquedas
    S.sort(key=sortCriteria)

    # Se calcula a^t*s mod p y se busca si existe en la lista
    # si existe, se ha encontrado solución (t*s-i)
    for t in range(1, s+1):
        aux = potenciaModular(a, t*s, p)
        i = busquedaBinaria(S, aux)
        if i != -1:
            return t*s - i

    return False

###################################################
###         Algoritmo ro de Pollard             ###
###################################################


"""
    Dado un elemento de la sucesión ro Pollard y a, b y p
    se genera el siguiente elemento de la sucesión
    como una lista con 3 elementos: xi, ai, bi
"""


def generaSucesion(elem, a, b, p):
    s = elem[0] % 3
    sucesor = []

    if s == 1:
        sucesor.append((elem[0]*b) % p)
        sucesor.append(elem[1])
        sucesor.append(elem[2]+1)
    elif s == 0:
        sucesor.append((elem[0]**2) % p)
        sucesor.append((elem[1]*2) % (p-1))
        sucesor.append((elem[2]*2) % (p-1))
    else:
        sucesor.append((elem[0]*a) % p)
        sucesor.append(elem[1]+1)
        sucesor.append(elem[2])

    return sucesor


"""
    Dada una sucesión del algoritmo ro Pollard, se busca
    elem en la sucesión y, si se encuentra, se devuelve la posicion
"""


def buscaEnSucesion(sucesion, elem):
    for x in range(len(sucesion)):
        if sucesion[x][0] == elem[0]:
            return x

    return -1


"""
    Dado un conjunto sol de soluciones a una congruencia
    se devuelve aquel que cumpla a^sol[x] = b mod p
"""


def compruebaSoluciones(sol, a, b, p):
    for x in range(len(sol)):
        if potenciaModular(a, sol[x], p) == b:
            return sol[x]

    return 0


"""
    Algoritmo ro de Pollard
"""


def roPollard(a, b, p):
    # creamos el conjunto de sucesiones
    sucesion = []
    encontrado = False
    i = 0

    # Generamos la sucesion hasta que encontremos una coincidencia
    # Cuando lo encontremos iremos avanzando con ambos elementos
    elem = [1, 0, 0]
    sucesion.append(elem)
    for x in range(1, p):
        elem = generaSucesion(elem, a, b, p)
        i = buscaEnSucesion(sucesion, elem)
        if i != -1:
            elem1 = sucesion[i]
            elem2 = elem
            encontrado = True
            break
        sucesion.append(elem)

    # Para cada par de elementos, generamos una congruencia
    # la resolvemos y, si es solucion, la devolvemos
    if encontrado:
        for x in range(i, p):
            a1 = elem2[2]-elem1[2]
            b1 = elem1[1]-elem2[1]

            sol = congruencia(a1, b1, p-1)

            if len(sol) == 1 and sol[0] != 0:
                return sol[0]
            elif len(sol) > 1:
                return compruebaSoluciones(sol, a, b, p)
            else:
                elem1 = generaSucesion(elem1, a, b, p)
                elem2 = generaSucesion(elem2, a, b, p)

    return False


# Ejecución de los 3 algoritmos para hacer el logaritmo
# log_a (b) mod p
def ejercicio1():
    a = 44455
    b = 11122
    p = 524387

    logaritmo = fuerzaBruta(a, b, p)
    print("Logaritmo calculado por fuerza bruta: ", logaritmo)

    logaritmo = pasoEnanoPasoGigante(a, b, p)
    print("Logaritmo calculado por paso enano - paso gigante: ", logaritmo)

    logaritmo = roPollard(a, b, p)
    print("Logaritmo calculado por ro Pollard: ", logaritmo)



#Factorizacion

def fermat(n):
    x = int(math.sqrt(n))
    x += 1
    y = x**2 - n

    while int(math.sqrt(y))**2 != y:
        x += 1
        y = x**2 - n

    y = int(math.sqrt(y))
    v = x+y
    u = x-y

    return v, u



def f_po(x,n):
    return (x**2 + 1)%n

def mcd_po(x1,x2,n):
    return math.gcd(x2-x1, n)

def pollard(n):
    x1, x2, mcd = 1,1,1
    
    while mcd == 1 :
        x1=f_po(x1,n)
        x2=f_po(f_po(x2,n),n)
        mcd = mcd_po(x1, x2, n)

    if(mcd == n):
        return 0,0

    return int(n/mcd),mcd
    

def ejercicio2():
    
    n = 1247629321213412335
    print(str(n).__len__())
    x,y = fermat(n)
    print("La factorizacion mediante Fermat de:", n, "es", x, "*",y, "\n")

    x, y = pollard(n)
    print("La factorizacion mediante Pollard de:", n, "es", x, "*", y)



#3.3 Raices cuadradas Modulares:

# ExponenteModulo eficiente, recibe a,b,m como parametros
# calcula a**b mod m y lo devuelve
def modExp(a, b, m):
    aux = 1
    while b > 0:
        if b % 2 == 1:
            aux = (aux * a) % m
        b = b // 2
        a = (a * a) % m
    return aux
# Comprueba si un número es primo probable mediante el test de Miller-Rabin


def millerRabin(n):
    s = n - 1
    u = 0

    while(s % 2 == 0):
        s = s//2
        u = u+1

    # Elegimos num aleatorio entre 2 y n-2
    a = randrange(2, n - 1)
    a = modExp(a, s, n)

    if a == 1 or a == n - 1:
        return True
    else:
        for i in range(1, u):
            a = (a * a) % n
            if(a == n - 1):
                return True
            elif(a == 1):
                return False
        return False


# Calcula las raices cuadradas modulo un primo,
# es decir, cuantas soluciones entre 1 y p-1 tiene  x**2_= a(mod p).
# En otras palabras , clacular en Zp las raices del polinomio x**2 - a.
# Como p es primo el numero de soluciones lo da el grado del pol, asi que el numero de raices es 0,1 ó 2
def simboloDeLegendre(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return (((-1)**(((p**2) - 1) // 8)) * simboloDeLegendre(a // 2, p))
    else:
        return ((-1)**((p - 1)*(a - 1) // 4) * simboloDeLegendre(p % a, a))


# Descompone num como 2**s * u
def bifact(num):
    u, s = num, 0
    while u % 2 == 0:
        u //= 2
        s += 1
    return s, u


def Jacobi(a, p):
    if((p % 2 != 0) and (p > 1)):
        # iniciamos simbolo jacobi
        simbolo = 1
        # 1º : aplicamos (a/p) = (a%p / p)
        aux = a % p
        # casos base
        if(aux == 0):
            return 0
        elif (aux == 1):  # 3º
            return 1
        elif aux == -1:  # 5º -1/p = -1
            return ((-1) ** ((p-1) // 2))

        s, u = bifact(aux)  # 2º : Calculamos u y s

        if(u > 0):  # 6º
            simbolo = ((-1)**((p**-1)//8))
            if(u % 2 == 0):
                simbolo *= simbolo
        if (s == 1):  # (1/p) = 1
            return simbolo
        elif (s == -1):  # -1/p = -1
            return simbolo*((-1) ** ((p-1)//2))
        if(p % 2 != 0):  # 7º
            return simbolo * Jacobi(p, s) * (-1)**((p - 1)*(s - 1)//4)


def Tonelli(a, p):
    # Primero comprobamos si p es primo
    if(millerRabin(p) is False):
        return 0
    elif(simboloDeLegendre(a, p) != 1):
        return 0
    else:
        n = 2
        while(simboloDeLegendre(n, p) == 1):
            n += 1

        u, s = bifact(p - 1)
        if(u == 1):
            r = ((a**((p+1) // 4)) % p)
            return p-r, r

        else:
            r = modExp(a, (s+1)//2, p)
            b = modExp(n, s, p)
            c = inversomodular(a, p)
            d = ((c*(r**2)) % p)
            j = 0
            while(j <= u-2):
                aux = modExp(d, 2**(u-2-j), p)
                if(aux == p-1):
                    r = ((r*b) % p)
                    d = ((d * (b**2)) % p)
                b = ((b**2) % p)
                j += 1
            return r, p-r


def ejercicio3():
    print("Raices modulares Simbolo Legendre de 7 y 2: ", simboloDeLegendre(2, 7),"\n")
    primo200 = 643808006803554439230129854961492699151386107534013432918073439524138264842370630061369715394739134090922937332590384720397133335969549256322620979036686633213903952966175107096769180017646161851573147596390153
    a = (79874651464197946554617816414614988764632231317987851315316884654651235689487531321545687724576452452456454**2) % primo200
    print("Raices modulares Tonelli: ", Tonelli(a, primo200))


ejercicio1()
ejercicio2()
ejercicio3()
