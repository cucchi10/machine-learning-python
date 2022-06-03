------------------------------------------------------------------------------
Ejercicio 1

1. Importar el archivo nba.csv adjunto en un programa de python.
2. Modificar el campo nombre por jugador e imprimir el dataframe.
3. Imprimirle un mensaje al usuario en el que se le pida que indique que desea hacer: Ver todos los jugadores, ver detalle por jugador,  ver el puntaje general o graficar
4. Si desea ver los jugadores, imprimirle solo los nombres de los jugadores.
5. Si desea ver detalle, pedirle el nombre del jugador y mostrarle todos sus datos.
6. Si desea ver el puntaje general, calcular la madia de los puntos de los jugadores.
7. Si quiere graficar, mostrarle el gráfico de puntos por jugador en una tamaño de 10x10 color verde con los textos indicativos.

------------------------------------------------------------------------------
Ejercicio 2

Desarrollar un programa que le pida un usuario una palabra de cuatro letras y la adivine por medio de un algoritmo genético. Para ello:

1. Importar la función choice de la librería random.
2. Importar la función fuzz de la librería fuzzywuzzy (previamente instalada desde CMD)
3. Declarar una lista con todos los caracteres el abecedario.
4. Pedirle al usuario que ingrese una palabra de cuatro caracteres. En caso que ingrese un largo incorrecto pedírselo nuevamente.
5. Desarrollar el algoritmo genético para intentar acercarse lo más posible al resultado.

------------------------------------------------------------------------------
Ejercicio 3

A partir de la tabla de datos adjunta, crear un sistema que sea capaz de predecir la temperatura promedio de la tierra para un año determinado.
Probar diversas  épocas y optimizadores  hasta alcanzar el mejor modelo para una red de una sola neurona.

------------------------------------------------------------------------------
Ejercicio 4

Crear un programa que, tras importar el archivo csv adjunto en un dataframe y lo recorra verificando que:
1. Todas las personas de las listas tengan su imagen. En caso que alguno no la tenga, eliminarlo del dataframe.
2. Verificar que todas las imágenes sean color. En caso que alguna se encuentre en escala de grises, imprimir un mensaje indicando que persona posee su imagen en escala de grises.
4. Al finalizar la normalización de las imágenes, el sistema le ofrecerá al usuario que:
 a. Vea la foto de un jugador, en cuyo caso le pedirá su número de camiseta y le mostrará la foto con su nombre completo como título y sin ejes.
 b. Ver todo el equipo, en cuyo caso le mostrará todas las fotos juntas en dos filas sin ejes.
c. Eliminar un jugador. En ese caso le pedirá el nombre y eliminará su registro del dataframe, del archivo csv y su foto.

------------------------------------------------------------------------------
Ejercicio 5

Almacenar una imagen aleatoria de las tres adjuntas
El sistema deberá mostrar la imagen por 5 segundos acompañado de un mensaje por terminal indicando el color del semáforo y si el usuario debe esperar, avanzar o detenerse según corresponda.

------------------------------------------------------------------------------

### Para:

### conversor de temp.py
carpeta:conversor de temp

### clasificador de ropa.py
carpeta: clasificador de ropa

### numeros escritos a mano.py
carpeta: identificador de numero

### reconocedor de perros y gatos old
carpeta detector de gyp old

### reconocedor de perros y gatos
carpeta detector de gyp

### Inicia un servidor en la carpeta
Este proyecto utiliza un modelo de Tensorflow.js, el cual para cargarse requiere que el acceso sea por medio de http/https.
Para eso puedes usar cualquier servidor, pero aquí hay una forma de hacerlo:
- Descarga Python en tu computadora
- Abre una línea de comandos o terminal
- Navega hasta la carpeta donde descargaste el repositorio
- Ejecuta el comando `python -m http.server 8000`
- Abre un explorador y ve a http://localhost:8000