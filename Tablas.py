# Tablas.py
# Autor: Alan Manzanares
# Fecha de Creacion: 17/09/2019


for a in range (1,11):
    titulo="tabla del {}"
    print(titulo.format(a))
    #Como no le puse argumentos a print se va marcar como un espacio entre lo escrito
    # Lo cual me ayuda a mostrar los datos de una forma mas ordenada 
    print()
    for m in range (1,11):
        close="{} x {} = {}"
        print(close.format(a,m,a*m))
else:
        #Al ingresar print sin algun argumento se hace un salto de espacio 
        # despues de concluir con las iteraciones que le indicamos previamente
            print()