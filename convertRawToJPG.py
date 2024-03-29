from cv2 import cv2 #hot fix for VSCode annoyance that cv2 isn't recognized
import os
import numpy as np
import glob

#VARIABLES TO CHANGE
DIRECTORY_NAME = "Cam_1"
#DIRECTORY_PATH = "/Users/jetwang/Desktop/Georgia_Tech_Classes/SNEL/Hess_Lab/spinnaker_python-2.2.0.48-cp37-cp37m-macosx_10_9_x86_64/Examples/" #add path to directory if not in same folder
DIRECTORY_PATH = "/Volumes/Extreme_SSD/5_27_21/"
IMG_HEIGHT = 1080
IMG_WIDTH = 1440
MONOCHROME = True
VIDEO_NAME = DIRECTORY_NAME

#CODE BODY
count = 0 #count the current file that is being converted
os.chdir(DIRECTORY_PATH)
NEW_DIRECTORY = DIRECTORY_NAME+"_TO_JPG"
os.mkdir(NEW_DIRECTORY)
os.chdir(DIRECTORY_NAME)
print("Converting...")
glob_results = glob.glob("*.raw")
glob_results = glob_results[:90001]
for file in glob_results:
    img = np.fromfile(file, dtype=np.uint8) #get .raw img from directory
    img = img.reshape(IMG_HEIGHT, IMG_WIDTH) #in order to convert from .raw to .jpg, need to provide original height and width of img
    if not MONOCHROME:
        img = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2RGB)

    os.chdir("../" + NEW_DIRECTORY)

    cv2.imwrite(file[:-4]+".jpg", img)

    os.chdir("../" + DIRECTORY_NAME)
    count = count+1
    if count % 1000 == 0:
        print("Current file: " + str(count))

print("Conversion complete.")

    

