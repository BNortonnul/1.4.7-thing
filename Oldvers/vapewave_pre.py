import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np

def image_conditional_2(image, l1, v1, l2, v2, l3, v3, directory=None):
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    for r in range(height): #greenchannel test
        for c in range(width):
            if img[r][c]>l1 and img[r][c]<l2:
                #img[r][c] = plt.to_rgba(arg, alpha=None)
                #print img[r][c][2]
                img[r][c]=v1
                #plt.plot(c,r,'ro-',alpha=0.0)
            if img[r][c]>l2 and img[r][c]<l3:
                #img[r][c] = plt.to_rgba(arg, alpha=None)
                #print img[r][c][2]
                img[r][c]=v2
                #plt.plot(c,r,'ro-',alpha=0.0)
            if img[r][c]>l3:
                img[r][c]=v3
    '''for r in range(420, 470):
        list = []
        list.append(sum(img[r][c]))
        for c in range(15, 161):
            if sum(img[r][c])>180:
                
                img[r][c]=[0,255,0]
        print list'''
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')