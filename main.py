import cv2
import sys
import os
import numpy as np
from punto1 import basicColor
path1=input("Ingrese la direccion del archivo")
image_name1=input("Ingrese el nombre del archivo")
xd=basicColor(path1,image_name1)
xd.displayProperties()
xd.makeBW()
h=int(input("Ingrese valor del hue"))
xd.colorize(h)
