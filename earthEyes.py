'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
hillaryclinton_file = os.path.join(directory, 'hillaryclinton.jpg')

# Open and show the hillaryclinton image in a new Figure window
hillaryclinton_img = PIL.Image.open(hillaryclinton_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(hillaryclinton_img, interpolation='none')

# Display hillaryclinton in second axes and set window to the right eye
axes[1].imshow(hillaryclinton_img, interpolation='none')
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

# Paste earth into right eye and display
# Uses alpha from mask
hillaryclinton_img.paste(earth_small, (500, 50), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(hillaryclinton_img, interpolation='none')
axes3[1].imshow(hillaryclinton_img, interpolation='none')
axes3[1].set_xlim(500, 500)
axes3[1].set_ylim(50, 100)
fig3.show()

'''hillaryclinton_img.paste(earth_small, (500, 50), mask=earth_small) 
# Display
fig4, axes4 = plt.subplots(1, 2)
axes3[0].imshow(hillaryclinton_img, interpolation='none')
axes3[1].imshow(hillaryclinton_img, interpolation='none')
axes3[1].set_xlim(500, 550)
axes3[1].set_ylim(50, 100)
fig3.show()'''
