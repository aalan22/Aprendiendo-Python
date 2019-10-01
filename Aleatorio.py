# Aleatorio.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019

#Vamos primero a usar la funcion import ya que es la que nos permite importar librerias en Python de las diferentes que existen 
import random
numero1=float(10.5)
#Despues de definir una variable float y asignarle un valor pasamos a darle una instruccion a python 
#el fin esque python nos de cifras aleatorias cada que ejecutemos nuestro programa en el ordenador
def funcion():
    numero2=float(random.randrange(1,10))
    #Se hara la suma de los numeros por medio de corchetes para agrupar los datos
    anuncio=("la suma entre los siguientes numeros es: {} y {} es {} ")
    print(anuncio.format(numero1,numero2,numero1+numero2))
funcion()
#Al ultimo se ejecutara la funcion cada vez que se lo pidamos a python