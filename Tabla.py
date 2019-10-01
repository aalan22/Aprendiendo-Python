# Tabla.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019

# la funcion for va permitirnos que se ejecute una parte del codigo en varias ocasiones 
# al momento de pedirle que haga un viaje entre un rango de valores 
#Se le pide a un usuario que ingrese un numero del 1 al 9 
numero=input ("Hey, Escribe un numero entre el 1 y el 9=")
numero=int(numero)
for D in range (1,11):
    close="{} x {} = {}" 
    #Python nos va mostrar la tabla del numero que ingresamos del 1 al 9
    print(close.format(numero,D,D*numero))