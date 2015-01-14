import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
hillaryclinton_file = os.path.join(directory, 'hillaryclinton.jpg')

# Open and show the hillaryclinton image in a new Figure window
hillaryclinton_img = PIL.Image.open(hillaryclinton_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(hillaryclinton_img, interpolation='none')

fig.show()

# Open, resize, and display logo
logo_file = os.path.join(directory, 'logo.png')
logo_img = PIL.Image.open(logo_file)
'''logo_small = logo_img.resize((89, 87)) #eye width and height measured in plt'''
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(logo_img)
'''axes2[1].imshow(logo_small)'''
fig2.show()

# Paste logo into right eye and display
# Uses alpha from mask
hillaryclinton_img.paste(logo_img, (580, 50), mask='none') 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(hillaryclinton_img, interpolation='none')
axes3[1].imshow(hillaryclinton_img, interpolation='none')
axes3[1].set_xlim(500, 450)
axes3[1].set_ylim(500, 450)
fig3.show()


