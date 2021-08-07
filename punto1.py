import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
class basicColor:

    def __init__(self,path,image_name):

        path_file = os.path.join(path, image_name)

        # Read the image
        self.image = cv2.imread(path_file)

        # Check the image is valid
        assert self.image is not None, "There is no image at {}".format(path_file)
    def displayProperties (self):
        shape=self.image.shape
        pixeles=shape[0]*shape[1]/1000000
        canales=shape[2]
        print("El número de pixeles es: "+str(pixeles)+"MP "+" Los canales son:"+str(canales))
    def makeBW(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret,Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Image", Ibw_otsu)
        cv2.waitKey(0)
    def colorize(self,h):
        if(0<h<179):
            image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            h1, s, v = cv2.split(image_hsv)
            h1=h*np.ones_like(s)
            image_hue = cv2.merge((h1, s, v))
            image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
            cv2.imshow("Image", image_hue_bgr)
            cv2.waitKey(0)
            return image_hue_bgr
        else:
            print("El valor de h es incorrecto")