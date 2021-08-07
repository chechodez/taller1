#inicialización de librerías
import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
class basicColor:#inicialización de clases

    def __init__(self,path,image_name):#constructor

        path_file = os.path.join(path, image_name)

        # lectura de imagen
        self.image = cv2.imread(path_file)

        # verifica si el archivo no está vacío
        assert self.image is not None, "There is no image at {}".format(path_file)
    def displayProperties (self):# método para ver las propiedades de la imagen
        shape=self.image.shape# se adquiere el alto, ancho de píxeles y el npumero de canales
        pixeles=shape[0]*shape[1]/1000000#se obtienen los megapíxeles
        canales=shape[2]#obtención de canales
        print("El número de pixeles es: "+str(pixeles)+"MP "+" Los canales son:"+str(canales))#se imprime el número de canales y megapíxeles
    def makeBW(self):#metodo conversión binaria de la imagen (Metodo Otsu)
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)#se pasa a blanco y negro la imagen
        ret,Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)#thresholding metodo otsu
        cv2.imshow("Image", Ibw_otsu)#se muestra la imagen
        cv2.waitKey(0)#pausa el código hasta que se cierre la imagen obsevada
    def colorize(self,h):#método para colorizar la imagen
        if(0<h<179):#asegura que el valor de hue esté entre los valores deseados
            image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)#conversión de bgr a hsv
            h1, s, v = cv2.split(image_hsv)#split and merge
            h1=h*np.ones_like(s)#matriz con todos los valores como el parámetro hue
            image_hue = cv2.merge((h1, s, v))#se forma una imagen con la matríz creada anteriormente
            image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)#se convierte a bgr nuevamente
            cv2.imshow("Image", image_hue_bgr)#se meustra la imagen
            cv2.waitKey(0)#pausa el código hasta que se cierre la imagen obsevada
            return image_hue_bgr#regresar la imagen
        else:
            print("El valor de h es incorrecto")#se imprime que el valor de hue es incorrecto
