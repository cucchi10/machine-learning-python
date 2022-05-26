import random
from random import choice

from fuzzywuzzy import fuzz

from string import ascii_lowercase

ABECEDARIO = list(ascii_lowercase) # no tiene ñ

#ABECEDARIO= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

# para ver que esten las 27 letras XD
#print(len(ABECEDARIO))

# cantidad de poblacion, seleccionados para herencia y generaciones

PERSONA = 10

SELECCION =5

GENERACION = 100

#------------------------- Seccion Mennu ----------------------------

# menu principal, reviso que sean 4 slots y luego reviso que sean solo letras


def menu():
    userPalabra = input('''Ingrese una palabra de 4 caracteres
    
''').lower()
    if len(userPalabra) == 4:
        if userPalabra.isalpha():
            return desarmarUserPalabra(userPalabra), userPalabra
        else:
            print('No se Ingresaron solo letras...')
            menu()
    else:
        print('No se Ingreso una palabra de 4 caracteres...')
        menu()


# guardo la input del user en una lista separada por letras


def desarmarUserPalabra(userPalabra):
    palabraDesarmada = []

    for i in userPalabra:
        palabraDesarmada.append(i)

    return palabraDesarmada

#------------------------- Fin Seccion Mennu ----------------------------


# creo mi primera poblacion de palabras -- solo se usa 1 vez

def crearPoblacion():  
    grupoIndividuos = []

    for i in range(PERSONA):
        individuo=[]
        for i in range(4):
            individuo.append(choice(ABECEDARIO))
        grupoIndividuos.append(individuo)

    generacionesPrint(grupoIndividuos,-1)
    return grupoIndividuos


#selecciono los 2 mejores

def seleccionar(palabraDesarmada, grupoIndividuos):

    totalNumeros = []
    for i in grupoIndividuos:
        numerosSuerte = []
        for z in range(4):
            suerte=fuzz.ratio(palabraDesarmada[z],i[z])
            numerosSuerte.append(suerte)
        totalNumeros.append(sum(numerosSuerte)/len(numerosSuerte))

    
    seleccionados=[]

    for i in range(SELECCION):
        max=-1
        indice = -1
        for indx, numero in enumerate(totalNumeros):
            if numero > max:
                max=numero
                indice=indx
        if not indice == -1: 
            seleccionados.append(grupoIndividuos[indice])
            totalNumeros.pop(indice)

    seleccionadosPrint(seleccionados)

    return seleccionados


# herencia

def heredar(x, seleccionados, palabraDesarmada):
    cambiarSuerte(seleccionados, palabraDesarmada)

    grupoIndividuos=[]

    for i in range(PERSONA):
        individuo=[]
        for z in range(4):
            indiceRandonSeleccionado= random.randint(0, len(seleccionados)-1)
            individuo.append(seleccionados[indiceRandonSeleccionado][z])
        grupoIndividuos.append(individuo)

    generacionesPrint(grupoIndividuos, x)

    return grupoIndividuos


# cambio las letras que tienen un acierto de 0

def cambiarSuerte(seleccionados, palabraDesarmada):

    totalNumeros = []

    for i in seleccionados:
        numerosSuerte = []
        for z in range(4):
            suerte=fuzz.ratio(palabraDesarmada[z],i[z])
            numerosSuerte.append(suerte)
        totalNumeros.append(numerosSuerte)
    
    for i in totalNumeros:
        for z in range(4):
            if i[z] == 0:
                seleccionados[totalNumeros.index(i)][z] = choice([letra for letra in ABECEDARIO if letra != seleccionados[totalNumeros.index(i)][z]])
    return seleccionados



# para ver si ya encontramos la palabra

def validar(seleccionados, userPalabra):

    validados = [''.join(letras) for letras in seleccionados]

    for palabra in validados:
        numeroEvaluado = fuzz.ratio(userPalabra,palabra)
        if numeroEvaluado == 100:
            return True 
    return False 


# comparacion de los 2 finalistas

def resultado(seleccionados,userPalabra):

    validados = [''.join(letras) for letras in seleccionados]

    valorPalabra= []


    for palabra in validados:
        valorPalabra.append(fuzz.ratio(userPalabra,palabra))

    
    for indx, numero in enumerate(valorPalabra):
        maximo=max(valorPalabra)
        if numero == maximo:
            print(f'''El Ganador es: 
{validados[indx]}
con {numero} % de semejanza''')


# print de generaciones

def generacionesPrint(generacionprint, generacion):
    grupos = []
    for x in range(len(generacionprint)):
        grupo = []
        for letra in generacionprint[x]:
            grupo.append(letra)
        grupos.append("".join(grupo))
    print(f'''La Generacion {generacion+1} es:
{" ".join(grupos)}''')


# prit seleccionados

def seleccionadosPrint(seleccionprint):
    grupos = []
    for x in range(len(seleccionprint)):
        grupo = []
        for letra in seleccionprint[x]:
            grupo.append(letra)
        grupos.append("".join(grupo))
    print(f'''Los Seleccionados son:
{" ".join(grupos)}''')


#funcion main

def main():
    grupoLetras, userPalabra =  menu()
    poblacion = crearPoblacion()   
    for i in range(GENERACION):
        seleccionados =  seleccionar(grupoLetras, poblacion)
        validacion = validar(seleccionados, userPalabra)
        if not validacion:
            poblacion= heredar(i, seleccionados, grupoLetras)
        else:
            return resultado(seleccionados,userPalabra)
    resultado(seleccionados,userPalabra)


if __name__ == '__main__':
    main()