# Acumulado.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019

#Para comenzar hacemos declaracion de variables o valores para fines de trabajo, lo cual nos ayudara con nuestro codigo
acumulado=int(0)
numero=str("")
# Como podemos ver se coloco True que es una condicion de verdad acompañada del While, 
# los cuales hacen posible crear un ciclo sin terminacion alguna hasta que le demos un Break 
while True:
    numero=input("Hey, Ingresa un Numero Entero: ")
    if numero=="":
        #Se cerrara el ciclo si es un dato o numero vacio el programa reportara cuando se cumpla esa condicion
        print("Vacio. Salida del programa.")
        break
    else:
        # si se le da un caracter valido lo mostrara haciendo el calculo correspondiente
            acumulado+=int(numero)
            close="Monto acumulado: {}"
            print(close.format(acumulado))


