import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np
import operator

def overlay_image(image_to_show, image_to_add, directory=None):
    """Displays the PLT.image specified.
    """
    
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    print directory
    new_image = PIL.Image.open(directory + direcx + image_to_show)
    new_imager = PIL.Image.open(directory + direcx + image_to_show)
    new_imager.show()
    new_image2 = PIL.Image.open(directory + direcx + image_to_add)
    new_image2.show()
    width, height = new_imager.size
    print str(width) + " " + str(height)
    #print new_image
    #print new_image2
    #if image_to_show == "":
    #    print_directory_list2()
    #    return "Use one of these"
    new_image22 = new_image2.resize((width,height), PIL.Image.ANTIALIAS)
    new_image22.show()

    new_imager.paste(new_image22, (width, height), new_image22)
    new_imager.show()
    #cohrt = PIL.Image.blend(new_imager, new_image22, alpha=0.5)
    #cohrt.show()
