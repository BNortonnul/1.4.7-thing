import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np
import operator

def proto_modmask(original_image2, directory=None):
    if directory == None:
        directory = os.getcwd()
    original_image = PIL.Image.open(directory + "/" + original_image2)
    
    precent_of_side = .30 #prevent obsolete input from erroring
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    rows = height 
    columns = width
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(original_image)
    base_layer = PIL.ImageDraw.Draw(original_image)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    
    for r in range(155):
        for c in range(width):
            if sum(img[r][c])>500:
                rounded_mask[r][c]=[255,0,255]
    for r in range(420, 470):
        for c in range(125, 161):
            if sum(img[r][c])>500:
                rounded_mask[r][c]=[0,255,0]
    return image
    
    # Uncomment the following line to show the mask
    plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result

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
    
def show_image_new(image_to_show, directory=None):
    """Displays the PLT.image specified.
    """
    if directory == None:
        directory = os.getcwd()
    new_image = PIL.Image.open(image_to_show)
    if image_to_show == "":
        print_directory_list2()
        return "Use one of these"

    fig, axes = plt.subplots(1, 1)
    axes.imshow(new_image, interpolation='none')
    
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
    
    
def blendimage_ms(i0, i1, directory = None):
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    print directory
    
    # suppose img1 and img2 are your two images
    img1 = PIL.Image.open(directory + direcx + i0)
    img2 = PIL.Image.open(directory + direcx + i1)
    
    # suppose img2 is to be shifted by `shift` amount 
    shift = (50, 60)

    # compute the size of the panorama
    nw, nh = map(max, map(operator.add, img2.size, shift), img1.size)

    # paste img1 on top of img2
    newimg1 = PIL.Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg1.paste(img2, shift)
    newimg1.paste(img1, (0, 0))

    # paste img2 on top of img1
    newimg2 = PIL.Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg2.paste(img1, (0, 0))
    newimg2.paste(img2, shift)

    # blend with alpha=0.5
    result = PIL.Image.blend(newimg1, newimg2, alpha=0.5)
    result.show()

def mergeimage(i0, i1, directory = None):
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()

    # suppose img1 and img2 are your two images
    img1 = PIL.Image.open(directory + direcx + i0)
    img2 = PIL.Image.open(directory + direcx + i1)
    
    # suppose img2 is to be shifted by `shift` amount 
    shift = (50, 60)

    # compute the size of the panorama
    nw, nh = map(max, map(operator.add, img2.size, shift), img1.size)
    width, height = img1.size
    print str(width) + " " + str(height)

    img2a = img2.resize((width,height), PIL.Image.ANTIALIAS)
    img2a.show()
    
    # paste img1 on top of img2
    newimg1 = PIL.Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg1.paste(img2a, shift)
    newimg1.paste(img1, (0, 0))

    # paste img2 on top of img1
    newimg2 = PIL.Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg2.paste(img1, (0, 0))
    newimg2.paste(img2a, shift)

    # blend with alpha=0.5
    result = PIL.Image.blend(newimg1, newimg2, alpha=0.5)
    result.show()

def devtest_resize(image_to_show, width, height, directory=None):
    """Displays the PLT.image specified.
    """
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    #width, height = new_image.size
    new_image = PIL.Image.open(directory + direcx + image_to_show)
    
    #wpercent = (width/float(img.size[0]))
    #hsize = int((float(img.size[1])*float(wpercent)))
    newer_image = new_image.resize((width,height), PIL.Image.ANTIALIAS)
    newer_image.show()
    return newer_image