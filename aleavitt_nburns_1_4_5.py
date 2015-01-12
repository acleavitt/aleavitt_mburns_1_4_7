import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def square_corners(original_image, percent_of_side):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner indent as a portion of the shorter dimension of original_image
    """
    #set the indent of the rounded corners
    width, height = original_image.size
    indent = int(percent_of_side * min(width, height)) # indent in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(indent,0),(width-indent,0),
                            (width-indent,height),(indent,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,indent),(width,indent),
                            (width,height-indent),(0,height-indent)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.polygon((0,0, 2*indent, 2*indent), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.polygon((width-2*indent, 0, width,2*indent), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.polygon((0,height-2*indent,  2*indent,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.polygon((width-2*indent, height-2*indent, width, height), 
                            fill=(0,127,127,255))
    ''' #bottom right
    drawing_layer.polygon((0,0), 2*indent, 2*indent),
                            fill=(0, 127, 127, 255)) '''
                         
    # Uncomment the following line to show the mask
    #plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
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

def square_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
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
        
        # Round the corners with indent = 30% of short side
        new_image = square_corners(image_list[n],.30)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)    