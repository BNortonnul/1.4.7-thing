import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np

def proto_modmask(original_image, overlay_image):
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
                img[r][c]=[255,0,255]
    for r in range(420, 470):
        for c in range(125, 161):
            if sum(img[r][c])>500:
                img[r][c]=[0,255,0]
    return image
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
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
        print print_directory_list2()
        return "Use one of these"

    fig, axes = plt.subplots(1, 1)
    axes.imshow(new_image, interpolation='none')
