# Compara.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019


#Este espacio sirve para pedirle al usuario que nos proporcione dos numeros para asi poder compararlos 
numeroA=input("NumeroA:")
numeroB=input("NumeroB:")
close="Numeros ingresados: {} y {}. {}."
#Esta condicion se cumplira siempre y cuando sean iguales los numeros que ingresaste
if (numeroA==numeroB):
    print(close.format(numeroA, numeroB,"Hey, los numeros que pusiste son iguales"))
else:
    if numeroA>numeroB:
        #Esta condicion se cumplle si un numero ingresado es mayor que el otro en este caso el primero
        print(close.format(numeroA, numeroB,"Hey, el primer numero que ingresaste es mayor"))
    else:
        #Esta condicion se cumple cuando el numero mayor ingresado es el segundo 
        print(close.format(numeroA, numeroB,"Hey, el segundo numero que ingresaste es mayor"))