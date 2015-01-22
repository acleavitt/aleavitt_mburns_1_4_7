import PIL
import matplotlib.pyplot as plt
import os.path              

def modify_image(original_image): 
    # Open the files in the same directory as the Python script
    #directory = os.path.dirname(os.path.abspath(__file__))  
    #picture_file = os.path.join(directory, original_image)
    
    

    # Open and show the picture image in a new Figure window
    original_image = PIL.Image.open(original_image)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original_image, interpolation='none')
    width, height = original_image.size
    percentage_top = int(height*.05)
    percentage_side = int(width*.05)


    # Display picture in second axes and set window to the right eye
    axes[1].imshow(original_image, interpolation='none')
    axes[1].set_xticks(range(600, 0, 100))
    axes[1].set_xlim(600, 0) #coordinates measured in plt, and tried in iPython
    axes[1].set_ylim(400, 0)
    fig.show()

    # Open, resize, and display earth
    #earth_file = os.path.join(directory, 'earth.png')
    earth_img = PIL.Image.open('earth.png')
    earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
    fig2, axes2 = plt.subplots(1, 2)
    axes2[0].imshow(earth_img)
    axes2[1].imshow(earth_small)
    fig2.show()

    #Open,resize, and display the abstract corner
    #abstract_file = os.path.join(directory, 'abstract.png')
    abstract_img = PIL.Image.open('abstract.png')
    abstract_small = abstract_img.resize((89, 87))
    fig4, axes4 = plt.subplots(1,2)
    axes4[0].imshow(abstract_img)
    axes2[1].imshow(abstract_small)
    fig4.show()



    # Paste whatever the logo ends up being in the bottom right
    # Uses alpha from mask
    original_image.paste(earth_small, ((width-100),(height-100)), mask=earth_small) 
    # Display
    fig3, axes3 = plt.subplots(1, 2)
    axes3[0].imshow(original_image, interpolation='none')
    axes3[1].imshow(original_image, interpolation='none')
    axes3[1].set_xlim(500, 500)
    axes3[1].set_ylim(50, 100)
    fig3.show()

    #Paste absract image in top left corner
    original_image.paste(abstract_small, (percentage_side, percentage_top), mask=0) 

    #Paste absract image in top right corner
    original_image.paste(abstract_small, (((width-percentage_side)-100), percentage_top), mask=0) 
    
    #paste absract image in bottom left corner
    original_image.paste(abstract_small, (percentage_side, ((height-percentage_top)-100)), mask=0) 

    # Display
    fig4, axes4 = plt.subplots(1, 2)
    axes3[0].imshow(original_image, interpolation='none')
    axes3[1].imshow(original_image, interpolation='none')
    axes3[1].set_xlim(500, 550)
    axes3[1].set_ylim(50, 100)
    fig3.show()
    

# Not working correctly, causes errors 
''' 
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
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



def modify_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'photos')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        
        new_image = modify_image(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)'''