#Importar librerias de math como ceil y sqrt (Son necesarias para el desarrollo de este script)
from math import ceil, sqrt
import random
 
"""Definición de la función que se va a encargar de buscar los valores 
a y b para que devuelva con un return los valores de a+b y de a-b, para ello
se aplicara FERMAT."""

def MetodoFermat(number):
   # Se coloca un condicional para solo permitir valores enteros positivos.
   # Es importante poner este condicionante por si alguien emplea un valor "number" inferior a 0.
    if(number<= 0):
        return [number] #Devolución del valor "number"
 
    # En este apartado se va a proceder a comprobar si n es un número par
    if(number & 1) == 0: 
        return [number / 2, 2]     
    a = ceil(sqrt(number))
    """Si la variable definida como number es una raiz perfecta, se llega a la conclusion de que 
    ambas raices cuadradas son sus factores"""
    if(a * a == number):
        return [a, a]
    while(True):
        val_b1 = a * a - number
        b = int(sqrt(val_b1))
        if(b * b == val_b1):
            global amesb
            amesb = a-b
            global amasb
            amasb = a+b
            break    
        else:
            a += 1        
    return [a-b, a+b]


def millerrabin(num_p):
    #Lo primero que se comprobara con la función de MillerRabin es si el número es impar.
    if 1&num_p==0:
        return ("No es primo")
        
    #Cogemos num_p y se le resta 1, se debe mostrar como 2 elevado al valor de potencia por num_imp que es impar.
    num_imp = num_p-1
    #En este apartado se procede a divir el valor anterior entre 2 hasta conseguir que el número sea impar.
    potencia = 0
    while 1&num_imp==0:
        potencia= potencia+1
        num_imp = num_imp >> 1
 
    for _ in range(20):#Bucle para poder minimizar la probabilidad de fallo al aplicar este algoritmo. El rango de comprobaciones es 20
        #Se elige un valor aleatorio llamado ale que cumpla la condicion que 2 sea menor o igual que este aleatorio y a su vez menor o igual a num_p-2
        ale = random.randint(2, num_p - 2)
        #Llamada a funcion encagargada de sacar el valor aleatorio elevado a numero impar y numero p obtenido anteriormente.
        ale = baseExpoModulo(ale,num_imp,num_p)
        #Condicionales para comprobar aleatorio.
        if ale == 1 or ale == num_p-1:
            return ("Es primo")
        else:
            for i in [1,1,potencia-1]:
                ale = baseExpoModulo(ale,2,num_p)
                if ale == num_p-1:
                    return ("Es primo")
                elif ale == 1:
                    return ("No es primo")
                i=i+1
            return ("No es primo")
     
     
def baseExpoModulo(base,exponente,modulo):
    """ 
        ESTA FUNCIÓN Se podia omitir e incorporar completamente en el procedimiento de miller-Rabin.
        Para un uso más sencillo y claro he decidido sacarla pero forma parte del procedimiento de Miller-Rabin
        Calcula base elevado al exponente correspondiente y multiplicado por módulo modulo.
        base,exponente,módulo: base^exponente mod módulo
        Calcula (base) (exponente) mod (módulo) en log (exponente) de tiempo.
        Devuelve lo mismo que se quiere introducir: base^exponente mod módulo
    """
    b = 1
    if exponente == 0:
        return b
 
    while exponente>=1:
        if exponente&1:
            b = (b*base)%modulo
        base =(base*base)%modulo
        exponente=exponente>>1
    return b     

# Esta parte se deja para mostrar el valor de Fermat y la llamada de las funciones de Miller-Rabin en cada uno de los factores obtenidos.
global num_idprimo
num_idprimo = 29128310549281
print("Se obtienen los siguientes factores del número: " + str(num_idprimo) + " Factores: " + str(MetodoFermat(num_idprimo)))
print("El número: " + str(amesb) + " " + millerrabin(amesb))
print("El número: " + str(amasb) + " " + millerrabin(amasb))


#Desarrollado por Adrián Hernández Ríos