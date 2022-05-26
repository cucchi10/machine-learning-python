#Linea 115 y 122 comentadas para no Borrar Nada Importante

# Importacion de Bibliotecas (El Buen Oscar)

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

from os import unlink

# Uso de datos del csv  

def ReadDf(df):
    jugadoresArray = df.to_numpy().tolist()
    jugadoresLongitud = len(jugadoresArray)
    return df, jugadoresLongitud, jugadoresArray
# ---

# Elimino los Jugadores que no tienen foto

def ArreglarArraysJugadores(df):
    df, jugadoresLongitud, jugadoresArray = ReadDf(df)
    i = 0
    while i < jugadoresLongitud:
        try:
            linkUrl = f'fotos/{jugadoresArray[i][2]} {jugadoresArray[i][1]}.jpg'
            plt.imread(linkUrl)
        except:
            input(f'No se encuentra Imagen de {jugadoresArray[i][2]} {jugadoresArray[i][1]} y fue eliminado del sistema')
            indexJugador = df.index[df.num == jugadoresArray[i][0]]
            df = df.drop(indexJugador)
        i+=1
    df, jugadoresLongitud, jugadoresArray = ReadDf(df)
    input(df) # Imprimo el df sin el Eliminado
    return df, jugadoresLongitud, jugadoresArray
#---

# Buscar escala de grises

def EscalaGrises(jugadoresLongitud, jugadoresArray):
    i = 0
    while i < jugadoresLongitud:
        linkUrl = f'fotos/{jugadoresArray[i][2]} {jugadoresArray[i][1]}.jpg'
        imgJugadores = mpimg.imread(linkUrl)
        try:
            imgJugadores.shape[2]
        except:
            input(f'Imagen de {jugadoresArray[i][2]} {jugadoresArray[i][1]} es en Escala de Grises')
        i+=1
#---

# fotos de todos los jugadores

def FotoDeTodosLosJugadores(jugadoresLongitud, jugadoresArray):
    i = 0
    while i < jugadoresLongitud:
        linkUrl = f'fotos/{jugadoresArray[i][2]} {jugadoresArray[i][1]}.jpg'
        imgJugadores = plt.imread(linkUrl)
        plt.subplot(2, 6, (i+1))
        plt.axis("off")
        plt.title(f'{jugadoresArray[i][2]} {jugadoresArray[i][1]}')
        plt.imshow(imgJugadores)
        i+=1
    plt.show()
#---

# con nombre muestro jugador

def BuscarPorNombre():
    salir = False
    while salir == False:
        buscarJugador = input('Ingrese el Nombre y Apellido del Jugador a Buscar: ').lower()
        try:
            linkUrl = f'fotos/{buscarJugador}.jpg'
            imgJugador = plt.imread(linkUrl)
            plt.axis("off")
            plt.title(f'{buscarJugador}')
            plt.imshow(imgJugador)
            plt.show()
            salir = True
        except:
            input(f'No se encontro al jugador {buscarJugador}, intente nuevamente...')

# con numero muestro jugador

def NumeroCamiseta(jugadoresArray):
    salir = False
    while salir == False:
        buscarJugador = input('Ingrese el NUMERO del Jugador a Buscar: ').upper()
        for i in jugadoresArray:
            if i[0] == buscarJugador:
                index = jugadoresArray.index(i)
                linkUrl = f'fotos/{jugadoresArray[index][2]} {jugadoresArray[index][1]}.jpg'
                imgJugador = plt.imread(linkUrl)
                plt.axis("off")
                plt.title(f'{jugadoresArray[index][2]} {jugadoresArray[index][1]}')
                plt.imshow(imgJugador)
                plt.show()
                salir = True
        if salir == True:
            break
        else:
            input(f'No se encontro al jugador {buscarJugador}, intente nuevamente...')
#--

# Borrar un Jugador

def BorrarJugador(df, jugadoresArray):
    salir = False
    while salir == False:
        buscarJugador = input('Ingrese el Nombre y Apellido del Jugador a Borrar: ').lower()
        try:
            linkUrl = f'fotos/{buscarJugador}.jpg'
            #unlink(linkUrl)   #comentado para no Borrar Ninguna Imagen
            for i in jugadoresArray:
                nombreCompleto = f'{i[2]} {i[1]}'
                if nombreCompleto == buscarJugador:
                    indexJugador = df.index[df.num == i[0]]
                    df = df.drop(indexJugador)
                    jugadoresArray.remove(i)
                    #df.to_csv('argentina.csv', index=False)  #comentado para no Borrar Ningun Dato
                    input(f'Se Borro el DataFrame, CSV y Foto Del Jugador {nombreCompleto}')
                    input(df) #Imprimo el df sin el Eliminado
                    salir = True
                    main() #mando recursion de todo el programa luego de borrar a un Jugador del CSV
        except:
            input(f'No se encontro al jugador {buscarJugador}, intente nuevamente...')




# menu principal

def menu(df, jugadoresLongitud, jugadoresArray):
    opcion= (input('''
Menu Principal

1 - Ver Todos Los Jugadores En Una Foto Grupal
2 - Buscar Jugador Por Su Numero De Camiseta
3 - Buscar Jugador Por Su Nombre
4 - Eliminar Registro y Foto de un Jugador

5 - Salir

Ingrese su opcion:

'''))
    if opcion.isdigit():
        return seleccion(int(opcion), df, jugadoresLongitud, jugadoresArray)
    else:
        print('No se Selecciono un Numero')
        menu(df, jugadoresLongitud, jugadoresArray)
#---

# Continuacion del Menu

def seleccion(opcion,df, jugadoresLongitud, jugadoresArray):
    if opcion == 1:
        return FotoDeTodosLosJugadores(jugadoresLongitud, jugadoresArray)
    elif opcion == 2:
        return NumeroCamiseta(jugadoresArray)
    elif opcion == 3:
        return BuscarPorNombre()
    elif opcion == 4:
        return BorrarJugador(df, jugadoresArray)
    elif opcion == 5:
        print('BYE :D')
    else:
        print('''

Numero No valido...

Intente Nuevamente

''')
        menu(df, jugadoresLongitud, jugadoresArray)
#---



def main():
    df=pd.read_csv("argentina.csv")
    df, jugadoresLongitud, jugadoresArray = ArreglarArraysJugadores(df)
    EscalaGrises(jugadoresLongitud, jugadoresArray)
    menu(df, jugadoresLongitud, jugadoresArray)
    


if __name__ == "__main__":
    main()