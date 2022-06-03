import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator
import os
import numpy as np
import matplotlib.pyplot as plt

#Descarga y extracción del set de datos
print("Descargando ZIP de datos")
url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
carpeta_zip = tf.keras.utils.get_file('cats_and_dogs_filterted.zip', origin=url, extract=True)

#Variables para rutas en disco
carpeta_base = os.path.join(os.path.dirname(carpeta_zip), 'cats_and_dogs_filtered')
carpeta_entrenamiento = os.path.join(carpeta_base, 'train')
carpeta_validacion = os.path.join(carpeta_base, 'validation')

carp_entren_gatos = os.path.join(carpeta_entrenamiento, 'cats')  # imagenes de gatos para pruebas
carpeta_entren_perros = os.path.join(carpeta_entrenamiento, 'dogs')  # imagenes de perros para pruebas
carpeta_val_gatos = os.path.join(carpeta_validacion, 'cats')  # imagenes de gatos para validacion
carpeta_val_perros = os.path.join(carpeta_validacion, 'dogs')  # imagenes de perros para validacion

#Guardar el numero de datos de entrenamiento para cada cosa
num_gatos_entren = len(os.listdir(carp_entren_gatos))
num_perros_entren = len(os.listdir(carpeta_entren_perros))
num_gatos_val = len(os.listdir(carpeta_val_gatos))
num_perros_val = len(os.listdir(carpeta_val_perros))
total_entrenamiento = num_gatos_entren + num_perros_entren
total_val = num_gatos_val + num_perros_val

TAMANO_LOTE = 100
TAMANO_IMG = 150

#Aumento de datos (escala, rotacion, blabla)
print("Realizando aumento de datos")
image_gen_entrenamiento = ImageDataGenerator(
      rescale=1./255,
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

#Generacion de datos de entrenamiento FTW
data_gen_entrenamiento = image_gen_entrenamiento.flow_from_directory(batch_size=TAMANO_LOTE,
                                                     directory=carpeta_entrenamiento,
                                                     shuffle=True,
                                                     target_size=(TAMANO_IMG,TAMANO_IMG),
                                                     class_mode='binary')

#Generacion de datos de validacion
image_gen_val = ImageDataGenerator(rescale=1./255)

data_gen_validacion = image_gen_val.flow_from_directory(batch_size=TAMANO_LOTE,
                                                 directory=carpeta_validacion,
                                                 target_size=(TAMANO_IMG, TAMANO_IMG),
                                                 class_mode='binary')

#Modelo!
modelo = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(2)
])

#Compilación
modelo.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#Entrenar la red. Toma un buen rato! Ve por un café ;)
#Oye suscribete al canal!
print("Entrenando modelo...")
epocas=60
history = modelo.fit_generator(
    data_gen_entrenamiento,
    steps_per_epoch=int(np.ceil(total_entrenamiento / float(TAMANO_LOTE))),
    epochs=epocas,
    validation_data=data_gen_validacion,
    validation_steps=int(np.ceil(total_val / float(TAMANO_LOTE)))
)

print("Modelo entrenado!")



#Exportar el modelo en formato h5
modelo.save('detector de gyp old/perros-gatos.h5')


'''

#Convertir el archivo h5 a formato de tensorflowjs
mkdir tfjs_target_dir
tensorflowjs_converter --input_format keras perros-gatos.h5 tfjs_target_dir


Utilizarlo en un celular
Si quieres abrirlo en tu celular, no se puede solo poner la IP local de tu computadora y el puerto, ya que para usar la cámara se requiere HTTPS. Puedes hacer un túnel de HTTPS siguiendo los siguientes pasos

Descarga ngrok en tu computadora, y descomprímelo
Abre una línea de comandos o terminal
Navega hasta la carpeta donde descargaste ngrok
Ejecuta el comando ngrok http 8000
Es importante tener ambos activos: El servidor de python, y el túnel de ngrok
En la línea de comandos aparecerá un enlace HTTPS. Puedes entrar ahí con tu celular, no importa si no estás en la red local.
El túnel expira después de 2 horas creo, en dado caso solo reinicias ngrok
Abre un explorador en tu celular y ve al enlace HTTPS indicado

'''