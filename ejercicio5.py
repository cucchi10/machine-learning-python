import cv2
import random
import numpy
import imutils


seguir = True
contador = 0

while seguir == True :
    while contador <= 5:

        #random de algunos de los 3 semaforos con tamaño pequeño
        semaforoRandom=str(random.randint(1,3))
        img=cv2.imread(f'semaforo/{semaforoRandom}.png')
        img= cv2.resize(img,(300,400))

        # paso de bgr a hsv
        hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # defino rango min - max de colores
        lowerRed = numpy.array([0,50,120])
        upperRed = numpy.array([8,255,255])

        lowerYellow = numpy.array([18,70,120])
        upperYellow = numpy.array([25,255,255])

        lowerGreen = numpy.array([40,70,120])
        upperGreen = numpy.array([70,255,255])

        # defino las mascaras con sus colores respectivos
        maskRed = cv2.inRange(hsv, lowerRed, upperRed)
        maskYellow = cv2.inRange(hsv, lowerYellow, upperYellow)
        maskGreen = cv2.inRange(hsv, lowerGreen, upperGreen)

        # el color es buscado por su contorno en la imagen
        colorRed = cv2.findContours(maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        colorRed = imutils.grab_contours(colorRed)

        colorYellow = cv2.findContours(maskYellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        colorYellow = imutils.grab_contours(colorYellow)

        colorGreen = cv2.findContours(maskGreen, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        colorGreen = imutils.grab_contours(colorGreen)

        # si hay una coincidencia imprimo el color
        if colorRed:
            print('DETENERSE - ROJO')

        if colorYellow:
            print('ESPERAR - AMARILLO')

        if colorGreen:
            print('AVANZAR - VERDE')
        
        cv2.imshow("Semaforo",img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

        contador+=1
    opcion=input('Desea seguir con el Test?: Si/No ').lower()
    if opcion == "si":
        print('Se Continuan Con Los Test...')
        contador = 0
    else:
        seguir = False
        input('Muchas Gracias Por Su Test...')


