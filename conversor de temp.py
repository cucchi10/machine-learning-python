import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=300, verbose=False)
print("Modelo entrenado!")

resultado = modelo.predict([100.0])
print("Prediccion: 100 grados celsius son " + str(resultado) + " fahrenheit!")

#Exportar el modelo en formato h5
modelo.save('conversor de temp/celsius_a_fahrenheit.h5')

'''

#Instalar tensorflowjs para convertir el h5 a un modelo que pueda cargar tensorflowjs en un explorador
pip install tensorflowjs

#Convertir el archivo h5 a formato de tensorflowjs
mkdir tfjs_target_dir
tensorflowjs_converter --input_format keras modelo_exportado.h5 tfjs_target_dir


'''