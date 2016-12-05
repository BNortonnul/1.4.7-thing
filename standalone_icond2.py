import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np

def image_conditional_2(image, directory=None):
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    for r in range(155):
        for c in range(width):
            if sum(img[r][c])>500:
                img[r][c]=[255,0,255]
    for r in range(420, 470):
        for c in range(15, 161):
            if sum(img[r][c])>180:
                print sum(img[r][c])
                img[r][c]=[0,255,0]
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')