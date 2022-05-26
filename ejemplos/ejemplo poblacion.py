import random

#print(random.randint(0,10))


poblacion=5

seleccion=2

generaciones=3

individuos =[]

for i in range(poblacion):
    fuerza=random.randint(1,3)
    inteligencia=random.randint(1,3)
    velocidad=random.randint(1,3)
    aptitud=fuerza+velocidad+inteligencia
    individuos.append([fuerza, inteligencia, velocidad, aptitud])
    #print(individuos)

    print(f'''La primer generacion de individuos es: 
{individuos}''')

def seleccionar():
    global seleccionados
    seleccionados = []

    for i in range(seleccion):
        max=0
        for i in individuos:
            if i[3]>max:
                max=i[3]
                indice=individuos.index(i)
        seleccionados.append(individuos[indice])
        individuos.pop(indice)

    print(f'''Los seleccionados son:
{seleccionados}''')

def heredar():
    global individuos
    individuos=[]

    for i in range(poblacion):
        fuerza=seleccionados[random.randint(0,1)][0]
        inteligencia=random.randint(1,3)
        velocidad=seleccionados[random.randint(0,1)][2]
        aptitud=fuerza+velocidad+inteligencia
        individuos.append([fuerza, inteligencia, velocidad, aptitud])


    print(f'''La siguiente generacion de individuos es: 
{individuos}''')


for i in range(generaciones):
    seleccionar()
    heredar()

seleccionar()

if seleccionados[0][3]>seleccionados[1][3]:
    print(f'''El individuo final es: 
{seleccionados[0]}''')
else:
    print(f'''El individuo final es: 
{seleccionados[1]}''')