# Multiplo.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019 
 #Primero vamos a ingresar un numero el cual se va almacenar una vez que se haga la conversion a int
numero=int(input("Ingresa un numero entero: "))
#Va quedar guardada en modo booleano para poder
# asi hacer una evaluacion de los datos si se muestra como residual el cero nos arroja que el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# En mi caso use and, porque se resuelve de manera verdadera si se cumplen todas las condiciones verdaderas
# y or lo use porque a vces no todas son verdaderas y el se encarga de resolverlo 
# Hice el uso de parentresis porque he aprendido que sirven para indicarle a python diferentes acciones a seguir
# por ejemplo en este caso para marcar que una condicion es indepoendiente y las otras dos restantes tienen que estar juntas
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Hey. esto es correcto.")
else:
        print ("Hey, esto es incorrecto")
