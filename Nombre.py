# Nombre.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019


# Para que se pueda realizar con exito lo deseado debemos 
# usar la concatenacion que es un enlace de hechos que guardan una relacion logica en este caso nuestro nombre y apellido
nombre=input("Nombre:")
apellidos=input("Apellidos:")
#Se le va pedir a python que use las mayusculas para mostrar el nombre junto al apellido
nombreCompleto=nombre+" "+apellidos
nombreCompleto=nombreCompleto.upper()
#Usaremos print para pedirle a python que nos muestre 
# en pantalla nuestros datos transformados a lo que le pedimos
print(nombreCompleto)
