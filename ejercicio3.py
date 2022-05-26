import pandas as pd

import tensorflow as tf
from tensorflow import keras


# ------------- Menu -------------

def menu():
    opcion= (input('''
Ingrese el año a predecir:

'''))
    if opcion.isdigit():
        return int(opcion)
    else:
        print('No se Selecciono un Numero')
        menu()
# ------------- Fin Menu -------------

# ------------- Red Neuronal -------------

model= tf.keras.Sequential([keras.layers.Dense (units=1, input_shape=[1])])
              
#model.compile(optimizer=tf.keras.optimizers.RMSprop(0.00001), loss="mean_squared_error") # (0.1) valor a corregir, mas pequeños si se quiere mas precicion, pero toma mas epocas

model.compile(optimizer="RMSprop", loss="mean_squared_error")

# ------------- Fin Red Neuronal -------------

# ------------- Lectura y Creacion de Arrays -------------

df=pd.read_csv('clima.csv')

years=[]
temps=[]

for i in df.year:
    years.append(i)
for i in df.temp:
    temps.append(i)

# ------------- Fin Lectura y Creacion de Arrays -------------

# entrenamiento y prediccion de dato ingresado

historial = model.fit(years, temps, epochs=500, verbose=False) # quitar spam de entrenamiento

valor = menu()

print(model.predict([valor]))


#grafico para ver la correcion en las distintas epocas

import matplotlib.pyplot as plt
plt.figure(figsize=(6 , 6))
plt.xlabel("Epoca")
plt.ylabel("Perdida")
plt.title('Grafico de Perdida VS Epocas')
plt.plot(historial.history['loss'])
plt.show( )


'''
año  - grados
1998 - 15

SGD
1000 epocas - 1 sola neurona - optimizer default
1998 - nan
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - nan

RMSprop
1000 epocas - 1 sola neurona - optimizer default
1998 - 14.895935 // 1998 - 15.064319 (deja de corregir antes de las 100 epocas)
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 114.427864
1000 epocas - 1 sola neurona - optimizer (0.01) (demasiada correcion en menos de 20 epocas)
1998 - 24.99083
500 epocas - 1 sola neurona - optimizer (0.001) (en 50 epocas deja de corregir)
1998 - 12.965021
500 epocas - 1 sola neurona - optimizer (0.0001) ( 200 epocas y deja de corregir)
1998 - 13.929235
500 epocas - 1 sola neurona - optimizer (0.00001)
1998 - -2072.0952 (no termina de aprender, llego a su maximo)


Adam
1000 epocas - 1 sola neurona - optimizer default
1998 - 19.594606
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 14.553241
100 epocas - 1 sola neurona - optimizer (0.1) (nada de flutuacion a apartir de las 20 epocas)
1998 - 14.092761
500 epocas - 1 sola neurona - optimizer (0.01) (nada de flutuacion a apartir de las 20 epocas)
1998 - 14.156549
500 epocas - 1 sola neurona - optimizer (0.001) (necesito mas epocas)
1998 - -87.44461
1000 epocas - 1 sola neurona - optimizer (0.001)
1998 - 14.144967
1000 epocas - 1 sola neurona - optimizer (0.0001) (sigue aprendiendo)
1998 - -2227.7346
2000 epocas - 1 sola neurona - optimizer (0.0001) (sigue aprendiendo)
1998 - 1430.499 (no termina de aprender, llego a su maximo)


Adadelta
1000 epocas - 1 sola neruona - optimizer default
1998 - -3078.5593
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 14.424012
100 epocas - 1 sola neurona - optmizer (0.1) (curva como triangulo rectungo, aun sigue aprendiendo)
1998 - -1350.519
1000 epocas - 1 sola neurona - optmizer (0.1) (a partir de 100 epocas no se ajusta mas)
1998 - 14.0423765 
500 epocas - 1 sola neurona - optimizer (0.01) (sigue aprendiendo)
1998 - 1276.9467
1000 epocas - 1 sola neurona - optimizer (0.01) (sigue aprendiendo)
1998 - 2782.4673
2000 epocas - 1 sola neurona - optimizer (0.01) (sigue aprendiendo)
1998 - 2091.3142
5000 epocas - 1 sola neurona - optimizer (0.01) (sigue aprendiendo)
1998 - 220.176
10000 epocas - 1 sola neurona - optimizer (0.01) (sigue aprendiendo)
1998 - -1467.6981 (no termina de aprender, llego a su maximo)

Adagrad
1000 epocas - 1 sola neurona - optimizer default
1998 - -1540.5597

Adamax
1000 epocas - 1 sola neurona - optimizer default
1998 - 14.131849
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 14.374778
100 epocas - 1 sola neurona - optimizer (0.1) (con 20 epocas ya no hay ajustes)
1998 - 14.115571
500 epocas - 1 sola neurona - optimizer (0.01) (200 epocas no hay cambios)
1998 - 14.1489935

Nadam
1000 epocas - 1 sola neurona - optimizer default
1998 - 14.158089
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 17.131693
100 epocas - 1 sola neurona - optimizer (0.1) (mucha fluctuacion en 100 epocas)
1998 - 22.63155
1000 epocas - 1 sola neurona - optimizer (0.01) (nada de fluctuacion a apartir de las 100 epocas, se podria decir que Nadam necesita un menor ajuste a su error para ser mas estable)
1998 - 14.084048
1000 epocas - 1 sola neurona - optimizer (0.001)
1998 - 14.1217
500 epocas - 1 sola neurona - optimizer (0.0001) (sigue aprendiendo, necesito mas epocas)
1998 - 994.5314
1000 epocas - 1 sola neurona - optimizer (0.0001) (sigue aprendiendo, necesito mas epocas)
1998 - -531.20483
2000 epocas - 1 sola neurona - optimizer (0.0001)
1998 - 13.990177


Ftrl
1000 epocas - 1 sola neurona - optimizer default
1998 - 3063.431
1000 epocas - 1 sola neurona - optimizer (0.1)
1998 - 14.1338215
100 epocas - 1 sola neurona - optimizer (0.01) (necesita mas epocas, sigue aprendiendo)
1998 - 8.632372
500 epocas - 1 sola neurona - optimizer (0.01)
1998 - 14.113135
1000 epocas - 1 sola neurona - optimizer (0.001) (es casi igual al de arriba)
1998 - 14.12249

'''