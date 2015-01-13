import PIL
import matplotlib.pyplot as plt
import os.path  

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
hillary_file = os.path.join(directory, 'Hillary_Clinton.jpg')


# Open and show the student image in a new Figure window
hillary_img = PIL.Image.open(hillary_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(hillary_img, interpolation='none')

width, height = hillary_img.size

# Open, resize, and display logo
logo_file = os.path.join(directory, 'feminist_logo.png')
logo_img = PIL.Image.open(logo_file)
logo_small = logo_img.resize((89, 87)) 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(logo_img)
axes2[1].imshow(logo_small)
fig2.show()

#paste logo onto hillary
hillary_img.paste(logo_small, ((width-10), (height-10)), mask=logo_small) 
