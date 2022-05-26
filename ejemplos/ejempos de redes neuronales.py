
import tensorflow as tf
from tensorflow import keras



# red de 1 neurona
# model= tf.keras.Sequential([keras.layers.Dense (units=1, input_shape=[1])])
# model.compile(optimizer="Adam", loss="mean_squared_error")


# red de 3 neuronas
oculta1=tf.keras.layers.Dense(units=3,input_shape=[1])
oculta2=tf.keras.layers.Dense(units=3)
capasalida=tf.keras.layers.Dense(units=1)

model=tf.keras.Sequential([oculta1,oculta2,capasalida])

model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss="mean_squared_error")


entradas=[0, 1, 10, 100]
salidas=[0, 200, 2000, 20000]

model.fit(entradas, salidas, epochs=100)


print(model.predict([200]))
