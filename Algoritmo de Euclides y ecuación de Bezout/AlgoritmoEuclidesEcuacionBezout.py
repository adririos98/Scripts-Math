#Solicitud de los valores en formato númerico para solicitarlos por consola.
num1 = int(input('Introduce el número de mayor tamaño: '))
num2 = int(input('Introduce el número de menor tamaño: '))
numbe1=num1
numbe2=num2
#Definición para ecuacion de Bezout de las variables de coe_x y coe_y y sus correspondientes listas.
x, coe_y = 0, 0
coe_x, y = 1, 1
varx_list = []
vary_list = []
print("ALGORITMO DE EUCLIDES")
print("Los números a los que se desea calcular el mcd son: {} y {}".format(num1,num2))
#Definicion de tablas para listas.
resto_list = []
cociente_list = [""]
numero_list = []
if num1<num2:
    num1,num2=num2,num1
    numero_list.append(num2)
    numero_list.append(num1)

numero_list.append(num1)
numero_list.append(num2)
resto=1
#Se crea el siguiente bucle para que siga operando hasta que el resto sea igual a 0, 
#en este caso la condición es distinto de cero para que siga iterando.
while resto != 0:
    # Si el num1 es inferior al num2, los invertimos
    # obtenemos el resto de la division
    resto=num1%num2
    cociente=num1//num2
    resto_list.append(resto)
    cociente_list.append(cociente)
    numero_list.append(resto)
    num1=num2
    num2=resto
    #Para dejar almacenado el valor del resto previo que es el mcd final.
    if resto!=0:
        resto_resu=resto 
    #Parte de la ecuación para sacar los valores de X e Y.
    #Coeficiente x:
    x, coe_x=coe_x - cociente * x, x
    varx_list.append(coe_x)
    #Coeficiente y:
    y, coe_y=coe_y - cociente * y, y
    vary_list.append(coe_y)
    #print("El resto es {}".format(resto_list))
    #print("El cociente es {}".format(cociente_list))

#FORMATO DE TABLA POR ALGORITMO DE EUCLIDES.
sep = '|{}|{}|{}|'.format('-'*10,  '-'*10,  '-'*10)
print('{0}\n| Cociente |  Número  |   Resto  |\n{0}'.format(sep))
for coci, nume, rest in zip(cociente_list, numero_list, resto_list):
    print('| {:>8} | {:>8} | {:>8} |\n{}'.format(coci, nume, rest,  sep))
print("El mcd es {}".format(resto_resu))

#Formateo para la salida de los valores de la ecuación de Bezout.
print("")
print("")
print("ECUACIÓN DE BEZOUT")
print ("{}x + {}y = {}".format(numbe1,numbe2,resto_resu))

#FORMATO DE TABLA POR ALGORITMO DE EUCLIDES.
sep = '|{}|{}|'.format('-'*12,  '-'*14)
print('{0}\n| Valor de x |  Valor de y  |\n{0}'.format(sep))
for varx, vary in zip(varx_list, vary_list):
    print('| {:>10} | {:>12} |\n{}'.format(varx, vary,  sep))

print ("X = ", coe_x, "Y = ", coe_y)

#Desarrollado por Adrián Hernández Ríos