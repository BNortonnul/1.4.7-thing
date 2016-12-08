import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
import numpy as np
import operator
import time
directory = os.getcwd() #get the basest directory
direcx = "/Documents/Demoimgs/"#specify directory beyond getcwd as default

def pause():
    programPause = raw_input("Press the <ENTER> key to continue...")
def new_path(strings):
    if strings == 0:
        print "Please specify new sub-directory."
        print"Example: /Documents/1.4.5 Images/"
    direcx = raw_input()
    
    if strings == 0:
        print direcx 
        print "Is this what you wanted? If not, restart this"
    return direcx

def layered_overwrite(image, filetype, changelist, showpercent, save):
    '''Based on a specific syntax, overwrites ranges of "brightness" with singular solid colors.
    '''
    directory = os.getcwd()
    filename = directory + direcx + image + filetype
    filename_noftype = directory + direcx + image
    if filetype != ".png": #If the filetype is not a png, then using this hacky PIL thing it makes it a png.
        conv = PIL.Image.open(filename)
        conv.save(filename_noftype + ".png")
        filename = directory + direcx + image + ".png"
    #print filename
    img = plt.imread(filename)

    if filetype != ".png":
        os.remove(filename_noftype + ".png") #Get rid of the PNG now that we have it in memory
    
    height = len(img) # PLT specific w/h retrievers
    width = len(img[0])
    
    if "samp" in changelist: #if it detects changelist is in fact a call for a sample, then it will replace it with pre-defined sample changecodes.
        if changelist == "samp_grayscale":
            changelist = [[2.5, [255, 255, 255]], [2.4, [244, 244, 244]], [2.3, [233, 233, 233]], [2.2, [222, 222, 222]], [2.1, [211, 211, 211]], [2.0, [200, 200, 200]], [1.9, [195, 195, 195]], [1.8, [188, 188, 188]], [1.7, [177, 177, 177]], [1.6, [166, 166, 166]], [1.5, [155, 155, 155]], [1.4, [144, 144, 144]], [1.3, [133, 133, 133]], [1.2, [122, 122, 122]], [1.1, [111, 111, 111]], [1.0, [100, 100, 100]], [0.9, [95, 95, 95]], [0.8, [88, 88, 88]], [0.7, [77, 77, 77]], [0.6, [66, 66, 66]], [0.5, [55, 55, 55]]]
        if changelist == "samp_rainbow":
            changelist = [[2.5, [255, 0, 0]], [2.0, [255, 0, 255]], [1.5, [0, 0, 255]], [1.0, [0, 255, 0]], [0.5, [255, 255, 0]], [0.0, [255, 128, 0]]]
        if changelist == "samp_mcdonald":
            changelist = [[1.9, [255, 255, 255]], [1.0, [255, 0, 0]], [0.0, [255, 255, 0]]]    
        if changelist == "samp_blue":
            changelist = [[2.5, [0, 0, 255]], [2.0, [0, 0, 222]], [1.5, [0, 0, 150]], [1.0, [0, 0, 100]], [0.5, [0, 0, 50]]]
        if changelist == "samp_swamp":
            changelist = [[2.5, [255, 255, 128]], [2.0, [255, 255, 255]], [1.5, [50, 255, 0]], [1.0, [0, 128, 0]], [0.5, [0, 100, 0]], [0.0, [0, 50, 0]]]
    for item in changelist:
        blist = []
        for item1 in item[1]:
            better_item = float(item1) / 255
            blist.append(better_item)           
        item[1]=blist
        #print blist
    for r in range(height):
        if r > 0 and showpercent == 1 and r % 4 == 0: #For every fourth new "row", it re-prints the percent.
            print (float(r) / float(height)) * 100
        for c in range(width):
            for item in changelist:
                #print item
                if sum(img[r][c])<changelist[len(changelist) - 1][0]:
                    break
                if sum(img[r][c])>=item[0]:  
                    img[r][c]=item[1] 
                    break
    # Create figure with 2 subplots
    fig, ax = plt.subplots(1, 1)
    ax.set_axis_off()
    # Show the image data in the first subplot
    if save == 0 or save == 1: #Show a preview of the image.
        ax.imshow(img, interpolation='none')
    if save == 1 or save == 2: #So PLT really likes adding useless borders to images lets do more PLT hacks and not have that happen
        plt.savefig(filename_noftype + "_immod0.png", bbox_inches='tight')
        crop1 = PIL.Image.open(filename_noftype + "_immod0.png")
        cropw, croph = crop1.size #Specify the size - it's not PLT so we have to do that again
        crop2 = crop1.crop((48, 18, cropw - 10, croph - 32)) #Might be a pixel off but the numbers work okay enough
        var = 1
        while os.path.isfile(filename_noftype + "_immod_" + str(var) + ".png") == True: #increment numbers so that it doesn't overwrite previous saves
            if os.path.isfile(filename_noftype + "_immod_" + str(var) + ".png") == False:
                crop2.save(filename_noftype + "_immod_" + str(var) + ".png")
            else:
                var += 1
        os.remove(filename_noftype + "_immod0.png")
    return "100" #percent thing stops at 99.???, so pretend it finishes anyway
    #print changelist
def overlay_image(image_to_show, image_to_add, save, showoff, direct, directory=None):
    """Overlays two images. Will resize the second to make sure it fits.
    """ 
    if directory == None:
        directory = os.getcwd()
    filename = directory + direct + image_to_show
    filename_noext = filename[:len(filename) - 4]
    filename2 = directory + direct + image_to_add #specify some directories so we don't have to do it later


    print directory
    image_to_modify = PIL.Image.open(filename)
    if showoff == 1:
        image_to_modify.show()
    unresized_overlay = PIL.Image.open(filename2)
    if showoff == 1:
        unresized_overlay.show()
    
    width, height = image_to_modify.size
    print str(width) + " " + str(height)
    
    resized_overlay = unresized_overlay.resize((width,height), PIL.Image.ANTIALIAS)
    if showoff == 1:
        resized_overlay.show()

    image_to_modify.paste(resized_overlay, (0,0), resized_overlay)
    if save == 0 or 1:
        image_to_modify.show()
    if save == 1 or 2:
        image_to_modify.save(filename_noext + "_immod.png")
        
def demo(skip_greeting):
    if skip_greeting == 0:
        print "Welcome to my cool image library. Let me set some stuff up."
    demo2()
def demo2():
    direct = new_path(1)
    image_to_show = "fine_art"
    image_to_show_f = "fine_art.jpg"
    filename = directory + direct + image_to_show_f
    filename_t = filename[:len(filename) - 4]
    print filename_t
    time.sleep(1)
    print "Alright, so the first thing. Let's make some abstract art."
    time.sleep(2)
    print "This is the first version of the image, btw."
    time.sleep(3)
    pause()
    im1 = PIL.Image.open(filename)
    im1.show()
    time.sleep(1)
    print "So, we will make this image a bit more interesting."
    print "layered_overwrite(filename, \".png\", \"samp_rainbow\", 1, 0)"
    pause()
    layered_overwrite(image_to_show, ".jpg", "samp_rainbow", 1, 0)
    demo21()
def demo21():
    time.sleep(1)
    print "How was that?"
    time.sleep(1)
    print "We're just getting started."
    time.sleep(2)
    print "Let's knock out a few others."
    pause()
    layered_overwrite("face", ".jpg", "samp_blue", 1, 0)
    pause()
    layered_overwrite("obama", ".jpg", "samp_mcdonald", 1, 0)
    pause()
    layered_overwrite("face2", ".jpg", "samp_swamp", 1, 0)
    demo3()
def demo3():
    print "One more..."
    layered_overwrite("Jon_tron", ".jpg", "samp_grayscale", 1, 0)