# Entrada.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019

#Usamos la variable booleana ya que nos da el pro de poder distinguir si lo que ingresamos es digito si como saber 
# si existen puntuaciones en la cifra si es asi se pretende que es un numero cuyo 
# esta compuesto por decimales
entrada=input()
#Se va marcar una entrada de dato para que el usuario ingrese el numero que esta pensando al momento y quiere evaluar
print(type(entrada))
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Si el dato ingresado por nosotros es correto no va decir python que se cumple la condicion y lo hicimos fenomenal
    print("Que bueno que acertaste si es un Entero, lo hiciste muy bien")
else:
    #El programa nos dira que estamos equivocados sino se cumple la condicion de esta manera
    print("Estas equivocado no ea un Entero, Estudia mas")