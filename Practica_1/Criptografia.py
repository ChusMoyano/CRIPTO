import random

random.seed(5)




def calc(a,b,m):
  num1=a
  num2=b
  mod=m
  s=1

  gola=11

  for i in range(0,num2):
    s=(s*num1)%mod

  print (s)

def calc2(a,b,m):
    num1=a
    num2=b
    mod=m
    s=1

    while num2>0:
      if((num2%2)==1):
        s=(s*num1)%mod
      num1=(num1*num1)%mod
      num2=num2//2

    return s


#Cuando sale 1 puede ser primo o no.

def calc3(n):
  num=n

  for i in range(0,n):
    s=i
    if((s*s)%n==1):
      print (s)


#Cuando el numero es primo impar. La ecuacion x²=1 mod p, tiene 2 soluciones
#Si p es producto de 2 primos impares, x²=1 mod n, tiene 4 soluciones
#Si p es producto de 3 primos impares, x²=1 mod n, tiene 8 soluciones

#calc3(25) #5*5
#calc3(45) #3²*5




#Teste de Miller Ralon
#¿M es primo?
#m-1 = 2^a * 5
#Elegimos a 2 <= a <= m-2
#vas elevando al cuadrado el exponente



def miller_Rabin(p):
    s = (p-1)/2
    u = 1

    while (s%2 == 0):
        s = (s)/2
        u += 1

    a = random.randint(2,p-2)
    a = calc2(a,s,p)

    if a == 1 or a == p-1:
        #print(p, "Es probable primo.")
        return 1

    else:
        for i in range(u-1):

            a = (a**2)%p

            if a == p-1:
                #print(p, "Es probable primo.")
                return 1
            if a == 1:
                #print(p, "No es primo.")
                return 0
        return 0

def miller_Rabin_checkSelf(p, max , flag):
    s = (p-1)/2
    u = 1

    posibles_primos = list()

    while (s%2 == 0):
        s = (s)/2
        u += 1

    for i in range(max):
        a = random.randint(2,p-2)
        a = calc2(a,s,p)

        print("Comprobamos si ",p, "es primo para a = ", a)

        if a == 1 or a == p-1:
            print(p, "Es probable primo.")
            res = 1
            posibles_primos.append(a)

        else:
            for i in range(u-1):

                a = (a**2)%p

                if a == p-1:
                    print(p, "Es probable primo.")
                    res = 1
                    posibles_primos.append(a)

                if a == 1:
                    print(p, "No es primo.")
                    res = 0

            if(a != 1 and a != p-1):
                print(p, "No es primo.")
                res = 0

    if(flag == 1):
        return posibles_primos

def miller_Rabin_checkSelf2(p, max , flag):
    s = (p-1)/2
    u = 1

    posibles_primos = list()

    while (s%2 == 0):
        s = (s)/2
        u += 1

    for i in range(max):
        b = random.randint(2,p-2)
        a = calc2(b,s,p)

        if a == 1 or a == p-1:
            res = 1
            posibles_primos.append(b)

        else:
            for i in range(u-1):

                a = (a**2)%p

                if a == p-1:
                    res = 1
                    posibles_primos.append(b)

                if a == 1:
                    res = 0

            if(a != 1 and a != p-1):
                res = 0

    if(flag == 1):
        return posibles_primos

def miller_Rabin_checkALL(p):
    s = (p-1)/2
    u = 1

    posibles_primos = list()

    while (s%2 == 0):
        s = (s)/2
        u += 1

    for i in range(2,p-1):
        a = i
        a = calc2(a,s,p)


        if a == 1 or a == p-1:
            #print(p, "Es probable primo.")
            res = 1

        else:
            for i in range(u-1):

                a = (a**2)%p

                if a == p-1:
                    #print(p, "Es probable primo.")
                    res = 1
                if a == 1:
                    #print(p, "No es primo.")
                    res = 0

            if(a != 1 and a != p-1):
                #print(p, "No es primo.")
                res = 0

        if(res == 1):
            posibles_primos.append(i)

    return posibles_primos

def testProb(n):
    r = miller_Rabin(n)
    if(r == 0):
        print(n, "No es primo.")
    if(r == 1):
        print(n, "Es probable primo.")


#n debe de ser impar
def siguiente_primo(p):
    n = p + 2
    m = miller_Rabin(n)

    while m != 1:
        n += 2
        m = miller_Rabin(n)

    print("El siguiente primo al",p, "es el ", n,".")


def primo_fuerte(n):
    return miller_Rabin((n-1)/2)


def siguiente_primo_fuerte(p):
        n = p + 2
        m = miller_Rabin(n)
        f = primo_fuerte(n)

        while m != 1 or f !=1:
            n += 2
            m = miller_Rabin(n)
            f = primo_fuerte(n)

        print("El siguiente primo fuerte al", p, "es el ", n,".")



def primo_n(n):
    a = random.randint(2**(n-1), 2**n)
    siguiente_primo_fuerte(a)





print("Ejercicio 1: ")
testProb(97)

print("Ejercicio 2: ")
miller_Rabin_checkSelf(561, 10, 0)

print("Ejercicio 3: ")
siguiente_primo(53)

print("Ejercicio 4: ")
siguiente_primo_fuerte(113)

print("Ejercicio 5: ")
primo_n(4)


print("Ejercicio 6.1: ")
primos1 = miller_Rabin_checkALL(6601)
print(primos1)


print("Ejercicio 6.2: ")
primos2 = miller_Rabin_checkALL(10585)
print(primos2)


print("Ejercicio 7.1: ")
print("Primos para: 1245172921232112343: ")
primos = miller_Rabin_checkSelf2(1245172921232112343, 100, 1)
print(primos)

print("Ejercicio 7.2: ")
print("Primos para: 9876126379174631985: ")
primos = miller_Rabin_checkSelf2(9876126379174631985, 100, 1)
print(primos)


print("Ejercicio 8.1: ")
print("Primos para: 3215031751: ")
primos = miller_Rabin_checkSelf2(3215031751, 100, 1)
print(primos)


print("Ejercicio 8.2: ")
print("Primos para: 2199733160881: ")
primos = miller_Rabin_checkSelf2(2199733160881, 100, 1)
print(primos)
