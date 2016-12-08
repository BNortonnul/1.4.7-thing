import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np
import operator

def get_images(directory=None): #import from mask.py
    """ Returns PIL.Image objects for all the images in directory.'''
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def print_directory_list2(directory=None):
    print get_images()[1]
def image_conditional_3legacy(image, l1, v1, l2, v2, l3, v3, directory=None):
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    for r in range(height):
        if r > 0:
            print (float(r) / float(height)) * 100
        for c in range(width):
            #list.append(sum(img[r][c]))
            if sum(img[r][c])>l1 and sum(img[r][c])<l2:
                img[r][c]=v1
                #print "switching to option 1"
            if sum(img[r][c])>l2 and sum(img[r][c])<l3 and sum(img[r][c]) != sum(v1):
                img[r][c]=v2
                #print "switching to option 2"
            if sum(img[r][c])>l3 and sum(img[r][c]) != sum(v2) and sum(img[r][c]) != sum(v1):
                img[r][c]=v3
                #print "switching to option 3"
        #print list
    '''for r in range(420, 470):
        list = []p
        list.append(sum(img[r][c]))
        for c in range(15, 161):
            if sum(img[r][c])>180:
                
                img[r][c]=[0,255,0]
        print list'''
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')
    print "is done now"
    
def image_conditional_35(image, l1, v1, l2, v2, l3, v3, directory=None):
    c1, c2, c3 = 9999, 9999, 9999
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    for r in range(height): #greenchannel test
        #list = []
        if r > 0:
            print (float(r) / float(height)) * 100
        for c in range(width):
            #list.append(sum(img[r][c]))
            if sum(img[r][c])>l1 and sum(img[r][c])<l2 and sum(img[r][c])<c1:
                img[r][c]=v1
                #print "switching to option 1"
            if sum(img[r][c])>l2 and sum(img[r][c])<l3 and sum(img[r][c]) != sum(v1) and sum(img[r][c])<c2:
                img[r][c]=v2
                #print "switching to option 2"
            if sum(img[r][c])>l3 and sum(img[r][c]) != sum(v2) and sum(img[r][c]) != sum(v1) and sum(img[r][c])<c3:
                img[r][c]=v3
                #print "switching to option 3"
        #print list
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')
    print "is done now"

def image_conditional_4jpg(image, changelist, directory=None):
    print "STOP CALLING THIS"
    '''inc = 0
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    print filename
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    previous_colors = []
    for r in range(height):
        #print previous_colors
        percenttick = 0 
        percenttick += 1
        if r > 0 and percenttick > 4:
            print (float(r) / float(height)) * 100
            percenttick = 0
        for c in range(width):
            ech = 0
            for item in changelist:
                #print item
                if sum(img[r][c])>item[0] and sum(img[r][c]) not in previous_colors and ech == 0: #and sum(img[r][c]) not in previous_colors:
                    ech = 1            
                    img[r][c]=blist
                    #print blist
                    #print item[1]
                    #if sum(img[r][c]) not in previous_colors:
                        #previous_colors.append(sum(blist))
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')
    print "100"
    print previous_colors'''
def image_conditional_4png(image, changelist, directory=None):
    inc = 0
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image
    print filename
    img = plt.imread(filename)
    height = len(img)
    width = len(img[0])
    previous_colors = []
    for r in range(height):
        #print previous_colors
        percenttick = 0 
        percenttick += 1
        if r > 0 and percenttick > 4:
            print (float(r) / float(height)) * 100
            percenttick = 0
        for c in range(width):
            ech = 0
            for item in changelist:
                #print item
                if sum(img[r][c])>item[0] and sum(img[r][c]) not in previous_colors and ech == 0: #and sum(img[r][c]) not in previous_colors:
                    ech = 1
                    blist = []
                    for item in item[1]:
                        inc = 0
                        better_item = float(item) / 255
                        blist.append(better_item)
                        '''if inc == 0:
                            print blist
                            inc = 1        '''            
                    img[r][c]=blist
                    #print blist
                    #print item[1]
                    #if sum(img[r][c]) not in previous_colors:
                        #previous_colors.append(sum(blist))
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    # Show the image data in the first subplot
    ax.imshow(img, interpolation='none')
    print "100"
    print previous_colors
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
    
    new_image22 = new_image2.resize((width,height), PIL.Image.ANTIALIAS)
    new_image22.show()

    new_imager.paste(new_image22, (0,0), new_image22)
    new_imager.show()
    #cohrt = PIL.Image.blend(new_imager, new_image22, alpha=0.5)
    #cohrt.show() #broked
