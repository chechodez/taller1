#inicialización de librerías
import cv2
import sys
import os
import numpy as np
from punto1 import basicColor#Se utiliza la clase basicColor
path1=input("Ingrese la direccion del archivo")#Solicita el ingreso de la dirección del archivo
image_name1=input("Ingrese el nombre del archivo")#Solicita el ingreso del nombre del archivo
xd=basicColor(path1,image_name1)#Se inicieliza la clase y se corre el contructor
xd.displayProperties()#Método display proyects muestra la cantidad de megapíxeles que tiene la imagen y los canales
xd.makeBW()#muestra la imagen en blanco y negro (Método Otsu)
h=int(input("Ingrese valor del hue"))#pide el valor de hue entre 0 y 179
xd.colorize(h)#muestra la imagen colorizada según el parámetro h
