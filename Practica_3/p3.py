#Factorizacion
import math

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
    n = 1247629321
    x,y = fermat(n)
    print("La factorizacion mediante Fermat de:", n, "es", x, "*",y)

    x, y = pollard(n)
    print("La factorizacion mediante Pollard de:", n, "es", x, "*", y)





ejercicio2()
