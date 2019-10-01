# Conversiones.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019


#Para comenzar vamos a declarar una variable, que incluya una cadena de digitos
numero="1234"
#La variable que vamos a usar se mostrara en su caso type y mas adelante se mostrara el tipo ya que ira cambiando 
#aunque se use el mismo tipo de datos en nuestro programa
print(type(numero))
numero=int(numero)
print(type(numero))
#Nos sera mostrado el resultado y asi culmina nuestro programa mostrando los valores 
#al usauario del ordenador
salida="Tu numero de orden es: {}"
print(salida.format(numero))

