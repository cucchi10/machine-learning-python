import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
#https://drive.google.com/file/d/19L5nMcr0H8dlsCGVRTNENwh_yAAwtOO3/view

categorias=["manzanas" , "ananas" , "kiwis"]
imagenes=[] #aca vamos a almacenar las imagenes como una lista con cada valor de px
labels=[] #labels es un lista con un valor para cada imagen 0 para las de la primer categoria, 1 para la segunda, 2 para la tercera

for index, i in enumerate(categorias):
    for k in range(1,10): #son 10 imagenes por carpeta
        img=cv2.imread(f'{i}/{k}.jpg',0) #almaceno cada imagen en escala de grises
        img=cv2.resize(img,(200,200)) #redimensiono cada imagen a 200 x 200 por la cantidad de neuronas de entrada
        img=np.asarray(img)#convierto la imagene en una lista de valor para cada px entre 0 y 255
        imagenes.append(img) #agrego cada lista a la lista imagenes
        labels.append(index) #agrego la indice a que categoria corresponde


def ModeloEstandar():
    model=tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(200,200)), #flattern entrega un vector 200 x 200 significa 40000 neuronas en la capa de entrada
        tf.keras.layers.Dense(128,activation="relu"), #densa es la conexion, 128 la canti de neuronas de la capa
        tf.keras.layers.Dropout(0.2), #apaga un 20% (por el 0.2) de las neuronas durante el entrenamiento aleatoriamente. Mejora el resultado
        tf.keras.layers.Dense(3,activation="softmax") #capa de salida, posee 3 opciones de salida
    ])
    return model


def ModeloConvolucion():
    model=tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), input_shape=(200,200,1), activation="relu"), #capa de convolucion tomas matrices de 3 x 3 px y genera 32 salidas, 200,200 tamaño 1 gris
        tf.keras.layers.MaxPooling2D(2,2), #capa de agrupamiento
        tf.keras.layers.Conv2D(64, (3,3), input_shape=(200,200,1), activation="relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Dropout(0.5), #apago el 50% de las neuronas
        tf.keras.layers.Flatten(), 
        tf.keras.layers.Dense(units=100, activation="relu"), #capa oculta de 100 neuronas
        tf.keras.layers.Dense(3, activation="softmax") #capa de salida
    ])
    return model

opcion=input('''
Ingrese el Modelo que desea:
1-Modelo Estandar
2-Modelo Convolucional
''')
if opcion == '1':
    model=ModeloEstandar()
else:
    model=ModeloConvolucion()

model.compile(optimizer="adam",
loss="sparse_categorical_crossentropy", 
metrics=["accuracy"]) # es la metrica mas usada, mide la cantidad de aciertos sobre el total - es la mas usada pero no recomendada con pocas imagenes 

#convierto a numpy areay (sin comas) porque el modelo asi lo requiere
imagenes=np.array(imagenes)
labels=np.array(labels)
model.fit(imagenes , labels , epochs=20)

test=cv2.imread("test.jpg",0) # imporoto la prieba en gris
test=cv2.resize(test,(200,200)) #la redimensiono
test=np.asarray(test) #lo convierto en arreglo de px
test=np.array([test]) #econvierto a un arreglo numpy  es un alista dentro de otra lista porque ese es el formato que tiene el set de imagenes)


resultado=model.predict(test)
print(resultado) #esto muestra una probabilidad mas el valor que mas se repita correcponde al label que sea
#resultado=[[0 1 0]]
print("Manzana:" , resultado[0][0]*100, "%" )
print("Anana:" , resultado[0][1]*100 , "%")
print("Kiwi:" , resultado[0][2]*100 , "%" )

print("Resultado final: " , categorias[np.argmax(resultado[0])])
