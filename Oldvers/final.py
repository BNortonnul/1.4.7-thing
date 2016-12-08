import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np
import operator
direcx = "/Documents/1.4.5 Images/"#specify directory beyond getcwd as default
def new_path():
    print "Please specify new sub-directory."
    print"Example: /Documents/1.4.5 Images/"
    direcx = raw_input()

def layered_overwrite(image, filetype, changelist, showpercent, save, directory=None):
    inc = 0
    direcx = "/Documents/1.4.5 Images/"#put a condition pls
    if directory == None:
        directory = os.getcwd()
    filename = directory + direcx + image + filetype
    filename_noftype = directory + direcx + image
    if filetype != ".png":
        conv = PIL.Image.open(filename)
        conv.save(filename_noftype + ".png")
        filename = directory + direcx + image + ".png"
    print filename
    img = plt.imread(filename)
    '''
    plt.axis('off')
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off') # labels along the bottom edge are off'''
    if filetype != ".png":
        os.remove(filename_noftype + ".png") #Get rid of the PNG now that we have it in memory
    height = len(img)
    width = len(img[0])
    previous_colors = ["obsolete"] #It's trash but removing it causes a lot of old stuff to break so eh
    for r in range(height):
        if r > 0 and showpercent == 1:
            print (float(r) / float(height)) * 100
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
    ax.set_axis_off()
    # Show the image data in the first subplot
    if save == 0 or save == 1:
        ax.imshow(img, interpolation='none')
    if save == 1 or save == 2:
        plt.savefig(filename_noftype + "_immod0.png", bbox_inches='tight')
        crop1 = PIL.Image.open(filename_noftype + "_immod0.png")
        cropw, croph = crop1.size
        crop2 = crop1.crop((48, 18, cropw - 10, croph - 32))
        crop2.save(filename_noftype + "_immod.png")
        #os.remove(filename_noftype + "_immod0.png")
    print "100"
    print previous_colors