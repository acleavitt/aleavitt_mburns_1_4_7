'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
picture_file = os.path.join(directory, 'picture.jpg')

# Open and show the picture image in a new Figure window
picture_img = PIL.Image.open(picture_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(picture_img, interpolation='none')
width, height = picture_img.size
percentage_top = int(height*.05)
percentage_side = int(width*.05)


# Display picture in second axes and set window to the right eye
axes[1].imshow(picture_img, interpolation='none')
axes[1].set_xticks(range(600, 0, 100))
axes[1].set_xlim(600, 0) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(400, 0)
fig.show()

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.show()

#Open,resize, and display the abstract corner
'''abstract_file = os.path.join(directory, 'abstract.png')
abstract_img = PIL.Image.open(abstract_file)
abstract_small = abstract_img.resize((89, 87))
fig4, axes4 = plt.subplots(1,2)
axes4[0].imshow(abstract_img)
axes2[1].imshow(abstract_small)
fig4.show()'''



# Paste whatever the logo ends up being in the bottom right
# Uses alpha from mask
picture_img.paste(earth_small, ((width-100),(height-100)), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(picture_img, interpolation='none')
axes3[1].imshow(picture_img, interpolation='none')
axes3[1].set_xlim(500, 500)
axes3[1].set_ylim(50, 100)
fig3.show()


#draw a border
draw.polygon([(

'''#Paste absract image in top left corner
picture_img.paste(abstract_small, (percentage_side, percentage_top), mask=earth_small) 
# Display
fig4, axes4 = plt.subplots(1, 2)
axes3[0].imshow(picture_img, interpolation='none')
axes3[1].imshow(picture_img, interpolation='none')
axes3[1].set_xlim(500, 550)
axes3[1].set_ylim(50, 100)
fig3.show()'''
