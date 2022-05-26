import pandas as pd
import matplotlib.pyplot as plt

# leo el archivo csv

df=pd.read_csv("nba.csv")

# cambio nombre de una columna

df=df.rename(columns={'nombre':'jugador'})

# armo unna lista para los jugadores

ds= []

for i in df.jugador:
    ds.append(i)

# longitud de la lista

longitud = len(df)


# menu principal

def menu():
    opcion= (input('''
Menu Principal

1 - Ver Todos Los Jugadores
2 - Ver Detalle Por Jugador
3 - Ver El Puntaje General
4 - Graficar

5 - Salir

Ingrese su opcion:

'''))
    if opcion.isdigit():
        seleccion(int(opcion))
    else:
        print('No se Selecciono un Numero')
        menu()      

# segun seleccion decido que hacer

def seleccion(opcion):
    if opcion == 1:
        return todosjugadores()
    elif opcion == 2:
        return jugadorver()
    elif opcion == 3:
        return mediajugadores()
    elif opcion == 4:
        return grafico()
    elif opcion == 5:
        print('BYE :D')
    else:
        print('''

Numero No valido...

Intente Nuevamente

''')
        menu()


# muestro la lista de jugadores

def todosjugadores():
    print(f'''
El Nombre De los Jugadores Son:

{df.jugador}''')
    input('''

Presione una tecla para continuar..
''')
    return menu()


# pido el nombre de un jugador, con un intento de 3 veces, si fallaste te envio al menu principal.

def jugadorver():
    salir = False
    contador = 0

    while salir == False:
        if contador <= 3:
            contador+=1
            i= 0
            player= input('''
Ingrese el Nombre Del Jugador que desea ver mas datos:

''') 
            while i < longitud:  
                if ds[i] == player:
                    print(f'''
            
La Fila del Jugador que selecciono es la siguiente: 

{df[df.jugador == player]}

''')
                    input('''

Presione una tecla para continuar..
''')
                    return menu()
                else:
                    i+=1
            else:
                print('''

Nombre No Encontrado...

Intente Nuevamente...
    ''')
        else:
            input('Demasiado intentos Fallidos...')
            salir=True
            return menu()


#media de jugadores

def mediajugadores():

    sumatotal = 0

    for i in df.puntos:
        sumatotal += i
    
    media=sumatotal/longitud

    print(f'''
La Media De Los Puntos De Los Jugadores Es:

{media} Puntos

''')
    input('''

Presione una tecla para continuar..
''')
    return menu()


# grafico

def grafico():

    x=df.jugador 

    y=df.puntos

    plt.figure(figsize=(10 , 10))

    plt.xlabel('Jugador')

    plt.ylabel('Puntos') 

    plt.title('Grafico Total')

    plt.bar(x,y, color='green') 

    plt.show( )

    input('''

Presione una tecla para continuar..
''')
    return menu()



def main():
    menu()


if __name__ == "__main__":
    main()