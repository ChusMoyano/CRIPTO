import Funciones as fn

#cesar cadena to lista +1

#texto con cifrado transposicion
def textoTrans():
    f = open("in/JesusMoyano1.txt","r")
    texto = f.read()

    frecuencia = fn.ngramas_repetidos(texto,3)
    print(frecuencia)
    """
    cadena = "QUE"
    x=fn.ocurrencias(cadena,texto,1)
    best_n=0
    
    for n in range(1,len(texto)):
        aux=fn.ocurrencias(cadena,texto,n)
        if(aux > x):
            print("MAYOR:",aux," N:",n)
            x=aux
            best_n=n
    print(x)
    print(best_n)
    cifra_n = int(len(texto)/best_n)
    print(len(texto)/best_n,"   ", cifra_n)
    print(fn.cifra_transposicion(texto,cifra_n))
    """
    texdescifrado=""+texto[0]
    pos = 0
    for i in range(len(texto)-1):
        pos=fn.siguiente(len(texto),25,pos)
        texdescifrado = texdescifrado + texto[pos]

    print(texdescifrado)



def textCesar():
    f = open("in/JesusMoyano2.txt", "r")
    texto = f.read()

    frecuencia = fn.ngramas_repetidos(texto, 1)
    print(frecuencia)

    texto_des = fn.cadenatolista(texto)
    texto_des[:] = [(x - 1)%27 for x in texto_des]
    lista = fn.listatocadena(texto_des)
    print(lista)


#pagina 23 subtitucion, ngramas para los 'que' ya que se repiten
def textSustitucion():
    f = open("in/JesusMoyano3.txt", "r")
    texto = f.read()
    
    replace = {'A': 'ñ', 'B': 'c', 'C': 'g', 'D': 't', 'E': 'x', 'F': 'p', 'G': 'k', 'H': 'q', 
    'I': 'r', 'J': 'y', 'K': 'a', 'L': 's', 'M': 'z','N': 'i','Ñ':'h', 'O': 'e', 'P': 'j',
     'Q': 'b', 'R': 'u', 'S': 'o', 'T': 'l', 'U': 'n', 'V': 'd',
      'W': 'v', 'X': 'm', 'Y': 'w', 'Z': 'f'}

   
    texto_descifrado = fn.cifra_sustitucion(texto,replace)
    print(texto_descifrado)


def gcd(a, b):
    if (b == 0):
        return a
    else:
         return gcd(b, a % b)


def textVigerene():
    f = open("in/JesusMoyano4.txt", "r")
    texto = f.read()
    
    frecuencia = fn.ngramas_repetidos(texto, 3)
    print(frecuencia)
    
    
    ocu = fn.apariciones("DJG", texto)
    separacion = ocu[0]
    #print(separacion)
    
    lejania = list()

    for i in range(len(separacion)-1):
        lejania.append(separacion[i+1] - separacion [i])

    #print(lejania)

    mcd = lejania[0]
    
    for x in lejania:
        mcd = gcd(mcd,x)
    
    bloques = fn.divide_cadena(texto,  mcd)
    
    """
    print(len(bloques))
    for i in bloques:
        print(fn.indice_coincidencia(i))
        print(fn.frecuencias(i))
        print(fn.ngramas_repetidos(i,1))
        print(" ")
    """
    clave = ["R","E","C","O","N","O","C","I","M","I","E","N","T","O"]
    
    
    print(fn.descifra_vigenere(texto,"RECONOCIMIENTO"))




textoTrans()
