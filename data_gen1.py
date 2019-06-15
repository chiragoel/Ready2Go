from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os, sys, time, threading, multiprocessing
from pylab import *
from PIL import *
import cv2
import glob
#import os

def image(cmd):
    print("Thread 1 \n")
    for img in glob.glob("C:/Users/DELL/Desktop/ready2go/downloads/images/*.jpg"):
    
        
         
    
        image= cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        image = cv2.resize(gray, max_size)
    
        new_im = image.ravel()
        
    
            
        for i in range(len(new_im)):
            wr = "%s , "%(str(new_im[i]))
            fw.write(wr)
        cl = "%s \n"%(str(0))
        fw.write(cl)
            
    


def lesion(cmd1):
    print("Thread 2 \n")   
    for img in glob.glob("C:/Users/DELL/Desktop/ready2go/downloads/Lesions images/*.jpg"):
    
        
         
        
        image= cv2.imread(img)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        image = cv2.resize(gray, max_size)
    
        new_im = image.ravel()
        
    
            
        for i in range(len(new_im)):
            wr = "%s , "%(str(new_im[i]))
            fw.write(wr)
        cl = "%s \n"%(str(1))
        fw.write(cl)
            
    
    
max_size = (10,10)
imagec = cv2.imread("C:/Users/DELL/Desktop/summer_sem/downloads/Cat images/2.jpg")
gray1 = cv2.cvtColor(imagec, cv2.COLOR_BGR2GRAY)
image1 = cv2.resize(gray1, max_size)

newim = image1.ravel()

a= "Class"
fw = open("input_img_pro.csv","w")
for i in range(len(newim)):
    col = "F" + str(i) +","
    fw.write(col)
classy = "%s \n"%(a)
fw.write(classy)

cmd=''
cmd1 = ''
print("\n...Thread start....")
t1 = threading.Thread(target=image , args=(cmd,))
t2 = threading.Thread(target=lesion , args=(cmd1,))
t1.start()
t2.start()
# Waiting to finish thread
while True:
  if threading.activeCount() == 1:
    break
  time.sleep(1)
  print ("Thread is still running...")

print("\n...All Thread ends....")

fw.close()